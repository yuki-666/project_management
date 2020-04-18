import os
import pandas as pd
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))
import config
import util.db as d

def get_project_superior():
    sql = 'select id as project_superior_id, name as project_superior_name from employee where career = 0'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.selectDB(sql)

def get_custom():
    # return all custom
    # return (custom_id, company_name)
    p = {}
    p['select_key'] = ['id as custom_id','company_name']
    p['tablename'] = 'customer'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.selectDB(d.selectSql(p))

def get_total_user(project_id=None):
    # total user in company
    sql = f'''select distinct id, name from employee;'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)

    if project_id is None:
        return res

    sql = f'''select distinct person_id from project_participant where project_id=\'{project_id}\';'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    worker_in = db.selectDB(sql)

    if worker_in == 'Empty':
        worker_in = []

    w_list = []
    for i in worker_in:
        w_list.append(i['person_id'])
    for i in res:
        if i['id'] in w_list:
            i['status'] = 1
        else :
            i['status'] = 0
    return res

def get_normal_account():
    # return username, name, career, department
    # login:id      | username  | password 
    # employee:id   | name      | gender    | career|superior_id   | tele      | department| mailbox
    sql = '''select login.username,employee.name,employee.career,employee.department
             from login join employee
             on login.id = employee.id;'''
    
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    
    for record in res:
        if record['career'] == '0':
            record['career'] = '项目上级'

        elif record['career'] == '1':
            record['career'] = '项目经理'
        
        elif record['career'] == '2':
            record['career'] = '普通工人'

        else:
            return 'error'

    return res

def get_super_account():
    sql = 'select username, password from super_login;'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.selectDB(sql)

def create_super_account(username, password):
    # return 0/1 (ok, username already exist)
    sql = f'''select username from super_login where username = '{username}';'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    if db.selectDB(sql) != 'Empty':
        return 1
    sql = f'''insert into super_login(username,password) values('{username}','{password}');'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(sql) 
    return 0

def create_normal_account(username, password, name, career, department):
    # return 0/1 (ok, username already exist)
    sql = f'''select username from login where username = '{username}';'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    if db.selectDB(sql) != 'Empty':
        return 1
    
    sql = f'''select max(id) from login;'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    uid = str(int(db.selectDB(sql)[0]['max(id)']) + 1)
    while len(uid) < 4:
        uid = '0' + uid

    sql = f'''insert into employee(`id`, `name`, career, department, delete_label) values('{uid}','{name}',{career},'{department}', 0);'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(sql)

    sql = f'''insert into login(`id`, `username`, `password`, delete_label) values('{uid}','{username}','{password}', 0);'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(sql)
    return 0

def delete_normal_account(username):
    # return 'error' if username not exist
    sql = f'''select id from login where username = '{username}';'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    if res == 'Empty':
        return 'error'
    # true delete, not set delete_label
    # 1. find uid
    uid = res[0]['id']
    # 2. delete in authority
    sql = f'''delete from authority where worker_id = '{uid}'; '''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(sql)
    # 3. delete in employee
    sql = f'''delete from employee where id = '{uid}'; '''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(sql)
    # 4. delete in login
    sql = f'''delete from login where id = '{uid}'; '''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(sql)
    # 5. delete in work_time
    sql = f'''delete from work_time where worker_id = '{uid}'; '''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(sql)
    # 6. delete in project_participant
    sql = f'''delete from project_participant where person_id = '{uid}'; '''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(sql)
    # 7. delete in function_partition
    sql = f'''delete from function_partition where worker_id = '{uid}'; '''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(sql)
    
    return 'ok'

def modify_normal_account(username, password, name, career, department):
    # return 'error' if username not exist
    sql = f'''select id from login where username = '{username}';'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    if res == 'Empty':
        return 'error'
    
    uid = res[0]['id']
    sql = f'''update login set password = '{password}' where id = '{uid}'; '''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(sql)
    sql = f'''update employee 
           set name = '{name}', career = '{career}', department = '{department}'
           where id = '{uid}'; '''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(sql)
    return 'ok'

def import_normal_account(file_name):
    data = pd.read_csv(file_name, sep='\t')
    data = data.values.tolist()

    # get max uid in db (uid = max(xxx))
    sql = f'''select max(id) from employee;'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    uid = int(db.selectDB(sql)[0]['max(id)'])

    for username, password, name, career, department in data:
        # get uid
        uid = uid + 1
        uid_str = str(uid)
        while len(uid_str) < 4:
            uid_str = '0' + uid_str

        # add data to db
        sql = f'''insert into employee(id,`name`, career, department) values('{uid_str}','{name}','{career}','{department}');'''
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        db.otherDB(sql)

        sql = f'''insert into login(id,username,password) values('{uid_str}','{username}','{password}');'''
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        db.otherDB(sql) 

    return 'ok'
