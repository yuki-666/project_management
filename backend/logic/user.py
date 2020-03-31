import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))
import config
import util.db as d

def get_project_superior():
    sql = 'select id, name from employee where career = 0'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    return res

def get_custom():
    # return all custom
    # return (custom_id, company_name)
    p = {}
    p['select_key'] = ['distinct id','company_name']
    p['tablename'] = 'customer'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.selectDB(d.selectSql(p))

def get_total_user(project_id=None):
    p={}
    p['select_key'] = ['id','name']
    p['tablename'] = 'employee'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(d.selectSql(p))
    # return total user in company
    if project_id is not None:
        # status: if user in project
        # return uid, name, status
        p['select_key'] = ['person_id']
        p['tablename'] = 'project_participant'
        p['key'] = ['project_id']
        p['value'] = [' = '+project_id]
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        worker_in = db.selectDB(d.selectSql(p))
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
    # TODO
    # return username, name, career, department
    pass

def create_super_account(username, password):
    # TODO
    # return 0/1 (ok, username already exist)
    pass

def create_normal_account(username, password, name, career, department):
    # TODO
    # return 0/1 (ok, username already exist)
    pass

def delete_normal_account(username):
    # TODO
    # true delete, not set delete_label
    # 1. find uid
    # 2. delete in authority
    # 3. delete in employee
    # 4. delete in login
    # 5. delete in work_time
    # 6. delete in project_participant
    # 7. delete in function_participant
    # return 'error' if username not exist
    return 'ok'

def modify_normal_account(username, password, name, career, department):
    # TODO
    # return 'error' if username not exist
    return 'ok'
