import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))
from datetime import datetime
from util.backend import change_time_format
import config
import util.db as d

def get_info(project_id=None, uid=None, keyword=None, detail=False, include_reject=False):
    # id | name      | status | customer_id | main_function
    #    | domain_id | tech   | project_leader_id | submit_date | reserve_date

    # check if only exist one type, or get all if == 0
    is_none_1, is_none_2, is_none_3 = project_id is not None, uid is not None, keyword is not None
    exist_param_count = is_none_1 + is_none_2 + is_none_3
    if exist_param_count > 1:
        return config.error_value

    # measure detail
    if detail == False:
        sql = '''select id, name, status, update_time from project'''
    else:
        sql = '''select project.id, project.name, project_superior_id, project.status, project.update_time, project.describe, project.scheduled_time, project.delivery_day, employee.name as project_superior_name, project.major_milestones, project.adopting_technology, project.business_area, project.main_function from project join employee on employee.id = project.project_superior_id '''

    if keyword is not None:
        like = '%'
        for i in range(len(keyword)):
            like = like + keyword[i]
            like = like + '%'

        sql_id = sql + ''' where id like '%s';''' % like
        sql_name = sql + ''' where name like '%s';''' % like
        if include_reject == False:
            sql_id = sql_id[:-1] + ' and status > 0;'
            sql_name = sql_name[:-1] + ' and status > 0;'

        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        res_id = db.selectDB(sql_id)
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        res_name = db.selectDB(sql_name)

        # merge and unique
        res = []
        if res_id != 'Empty':
            res += res_id
        if res_name != 'Empty':
            res += res_name
        res = [dict(j) for j in set([tuple(i.items()) for i in res])]
        return res

    if project_id is not None:
        sql += ''' where project.id = '%s' ''' % project_id
    elif uid is not None:
        sql += ''' join project_participant on project_participant.project_id = project.id where project_participant.person_id = '%s' ''' % uid

    # measure include_reject
    if include_reject == False:
        if exist_param_count == 0:
            # get all
            sql += ' where status > 0;'
        else:
            # project_id or uid
            sql += ' and status > 0;'

    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)

    if res == 'Empty':
        return []
    else:
        res = change_time_format(res, 'update_time')
        if detail:
            res = change_time_format(res, 'scheduled_time')
            res = change_time_format(res, 'delivery_day')

        return res

def get_info_include_work_time(uid):
    # not include reject project
    # return (id, name, status, update_time, remain_work_time)
    p={}
    p['select_key'] = ['project.id','project.name','project.status','project.update_time','work_time.remain as remain_work_time']
    p['tablename'] = 'project'
    p['join_tablename'] = ['work_time']
    p['on_key'] = ['work_time.project_id']
    p['on_value'] = ['project.id']
    # remain_work_time: remain largest work_time_id for same project_id
    p['sentence'] = f' where work_time.id in (select max(id) from work_time where worker_id = {uid} group by project_id)'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(d.selectSql(p))

    if res == 'Empty':
        return []
    else:
        res = change_time_format(res, 'update_time')
        return res

def confirm(project_id, status):
    # check if project status is 1 (pending), return 'error' if not
    sql = f'select status from project where id=\'{project_id}\';'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    if res[0]['status'] != 1:
        return 'error'

    # modify project status, from 1 to 0/2 (rejection/established)
    sql = f'update project set status=\'{status}\' where id=\'{project_id}\';'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.otherDB(sql)
    if res == 'ok':
        return 'ok'
    else:
        return 'error'

def modify(project_id, project_name, describe, status, scheduled_time, delivery_day, project_superior_id, major_milestones, adopting_technology, business_area, main_function):
    update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    sql = f'''
           update project set name=\'{project_name}\', `describe`=\'{describe}\', scheduled_time=\'{scheduled_time}\', update_time=\'{update_time}\',
           delivery_day=\'{delivery_day}\', project_superior_id=\'{project_superior_id}\', major_milestones={major_milestones},
           adopting_technology={adopting_technology}, business_area=\'{business_area}\', main_function=\'{main_function}\', status={status}
           where id=\'{project_id}\';'''

    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.otherDB(sql)
    return res

def create(uid, name, describe, development_type, scheduled_time, delivery_day, project_superior_id, custom_id, major_milestones, adopting_technology, business_area, main_function):
    # id:
    # '2020-1111-D-01'
    # 'date-customid-development_type-sequence_number'

    # date:取当前年份

    # sequence_number: 'date-customid-development_'为前缀的所有，取它们的sequence_number的max，再+1作为这次的sequence_number. 
    # 若是1位数前面添0, 若一个都没搜出来从1开始计数
    
    # id 由“四位年份-四位客户代码-研发类型 1 位（开发：D，维护：M，服务：S，其他：O）-顺序号 2 位”构成，且从外部系统导入，是一个选择项，不可更改。

    id = str(datetime.now().year) + '-' + str(custom_id) + '-' + development_type + '-' 
    p = {}
    p['select_key'] = ['max(id)']
    p['tablename'] = 'project'
    p['key'] = ['id']
    p['value'] = [''' like '%s' '''%(id+'%')]
    
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    id_pre = db.selectDB(d.selectSql(p))[0]['max(id)']
    sequence_number = int(id_pre[-2]+id_pre[-1])+1 if not id_pre == None else int(0)
    sequence_number = '0' + str(sequence_number) if  sequence_number<10 else  str(sequence_number)
 
    p.clear()
    p['tablename'] = 'project'
    p['column'] = ['id','`name`', '`status`', '`describe`', 'scheduled_time', 'delivery_day', 'project_superior_id', 'customer_id','major_milestones', 'adopting_technology', 'business_area', 'main_function', 'delete_label']
    p['values'] = [id + sequence_number,name, 1, describe, scheduled_time, delivery_day, project_superior_id, custom_id, major_milestones, adopting_technology, business_area, main_function, 0]
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    # add (project_id, person_id, 0000, 0) in project_participant
    if db.otherDB(d.insertSql(p)) == 'ok':
        p.clear()
        p['tablename'] = 'project_participant'
        #p['column'] = ['id','`name`', '`status`', '`describe`', 'scheduled_time', 'delivery_day', 'project_superior_id', 'customer_id','major_milestones', 'adopting_technology', 'business_area', 'main_function', 'delete_label']
        p['values'] = [id + sequence_number, uid, '0000', '0']
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        return db.otherDB(d.insertSql(p))
    return 'error'

def repush(project_id):
    # check status == 0 (rejection), return 'error' if not
    # set status to 1 (pending)
    sql = f'''update project set status=1 where status = 0 and id = '{project_id}';'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return 'error' if db.otherDB(sql) == 'none' else 'ok'

def get_function(project_id, worker_id=None):
    # get function list from project_id
    # worker_id and worker_name: list->str, split by ','
    if worker_id is None:
        # return function_id, function_name, worker_id, worker_name, parent_function_id
        sql = f'''
               select distinct id as function_id, function_name, parent_function_id
               from project_function
               where project_id=\'{project_id}\' and delete_label=0;'''
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        ret = db.selectDB(sql)

        for i in range(len(ret)):
            ret[i]['worker_id'] = ''
            ret[i]['worker_name'] = ''
            sql = f'''select e.id as worker_id, e.name as worker_name
                      from function_partition as f
                      join employee as e on f.worker_id=e.id
                      where f.project_id=\'{project_id}\' and f.function_id={ret[i]['function_id']};'''
            db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
            worker_list = db.selectDB(sql)
            if worker_list == 'Empty':
                continue
            for worker in worker_list:
                ret[i]['worker_id'] += worker['worker_id'] + ','
                ret[i]['worker_name'] += worker['worker_name'] + ','
            ret[i]['worker_id'] = ret[i]['worker_id'][:-1]
            ret[i]['worker_name'] = ret[i]['worker_name'][:-1]
        return ret
    else:
        # select with worker_id
        # return function_id, function_name
        p = {}
        p['select_key'] = ['f.id as function_id','f.function_name']
        p['tablename'] = 'project_function as f'
        p['join_tablename'] = ['function_partition as fp']
        p['on_key'] = ['f.id']
        p['on_value'] = ['fp.function_id']
        p['key'] = ['fp.worker_id']
        p['value'] = [' = '+worker_id]
    
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        return db.selectDB(d.selectSql(p))

def get_children_function(project_id, parent_function_id):
    # get function list from project_id, whose parent function id == parent_function_id
    # worker_id and worker_name: list->str, split by ','
    # return function_id, function_name, worker_id, worker_name, parent_function_id
    p = {}
    p['select_key'] = ['f.id','f.function_name','fp.worker_id','e.name','f.parent_function_id','rank() over(order by f.id)']
    p['tablename'] = 'project_function as f'
    p['join_tablename'] = ['function_partition as fp','employee as e']
    p['on_key'] = ['f.id','fp.worker_id']
    p['on_value'] = ['fp.function_id','e.id']
    p['key'] = ['f.project_id','f.parent_function_id']
    p['value'] = [' = '+project_id,' = '+parent_function_id]
    
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.selectDB(d.selectSql(p))

def get_project_member(project_id, function_id=None):
    sql = f'''select distinct employee.id as project_id, employee.name as worker_name
              from employee
              join project_participant on employee.id=project_participant.person_id
              where project_participant.project_id=\'{project_id}\';'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    return res if res != 'Empty' else []

    p={}
    p['select_key'] = ['worker_id']
    p['tablename'] = 'function_partition'
    p['key'] = ['id','project_id']
    p['value'] = [' = '+function_id,' = '+project_id]
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    worker_in = db.selectDB(d.selectSql(p))
    worker_list = []
    for i in worker_in:
        worker_list.append(i['worker_id'])
    for i in res:
        if i['id'] in worker_list:
            i['status'] = 1
        else:
            i['status'] = 0     
    return res

def add(a,index):
    if a[index] < '9' or (a[index] >= 'a' and a[index] < 'z') or (a[index] >= 'A' and a[index] < 'Z'):
        a[index] = chr(ord(a[index]) + 1)
    else :
        if a[index] == '9':
            a[index] = 'a'
        else :
            if a[index] == 'z':
                a[index] = 'A'
            else :
                if a[index] == 'Z':
                    a[index] = '0'
                    add(a,index - 1)

def add_function(project_id, parent_function_id, function_name):
    # new function id:
    # 1. last_function_id = max function_id starts with parent_function_id
    # 2. new_function_id = last_function_id + 1, 3 digits, each digit: 012……789abc……xyzABC……XYZ
    # worker_id not null

    sql = f'''select distinct max(id) from project_function where project_id=\'{project_id}\' and parent_function_id={parent_function_id};'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    last_function_id = db.selectDB(sql)[0]['max(id)']
    if last_function_id is None:
        last_function_id = '000'
    
    three_id = list(last_function_id[-3:])
    add(three_id, 2)
    if parent_function_id == '000':
        new_function_id = three_id[0] + three_id[1] + three_id[2]
    else:
        new_function_id = parent_function_id + three_id[0] + three_id[1] + three_id[2]

    sql = f'''insert into project_function(id, function_name, project_id, parent_function_id, function_status, delete_label)
              values(\'{new_function_id}\', \'{function_name}\', \'{project_id}\', \'{parent_function_id}\', 0, 0);'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.otherDB(sql)

def delete_function(project_id, function_id):
    # check if delete_label == 0, return 'error' if delete_label == 1
    sql = f'''select distinct delete_label from project_function where project_id=\'{project_id}\' and id={function_id} and delete_label=0;'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    if res == 'Empty':
        return 'error'

    # 1. set delete_label to 1
    # 2. set children functions' delete_label to 1 (children function: function id starts with function_id)
    # children function is parent of grandson function.when children function canceled,children of children function should also canceled
    sql = f'''update project_function set delete_label=1  where project_id=\'{project_id}\' and id like \'{function_id}%\' ;'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.otherDB(sql)

def modify_function(project_id, function_id, function_name, uid):
    #function_name
    p = {}
    p['tablename'] = 'project_function'
    p['set_key'] = ['function_name']
    p['set_value'] = [function_name]
    p['where_key'] = ['id','project_id']
    p['where_value'] = [' = '+function_id,' = '+project_id]
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    db.otherDB(d.updateSql(p))
    #uid
    uid = uid.split(',')
    p.clear()
    p['select_key'] = ['worker_id']
    p['tablename'] = 'function_partition'
    p['key'] = ['function_id','project_id']
    p['value'] = [' = '+function_id,' = '+project_id]
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    A = db.selectDB(d.selectSql(p))

    only_A = []
    A_and_B = []
    only_B = []
    for record in A:
        if record['worker_id'] in uid:
            A_and_B.append(record['worker_id'])
        else:
            only_A.append(record['worker_id'])
    only_B = list(set(uid)-set(A_and_B))
    #insert for only_B
    p.clear()
    p['tablename'] = 'function_partition'
    p['column'] = ['function_id','project_id','worker_id']
    p['values'] = [function_id,project_id,'unknown']
    for worker_id in only_B:
        p['values'][2] = worker_id
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        db.otherDB(d.insertSql(p))
    #delete for only_A
    p.clear()
    p['tablename'] = 'function_partition'
    p['key'] = ['function_id','project_id','worker_id']
    p['value'] = [' = '+function_id,' = '+project_id,'unknown']
    for worker_id in only_A:
        p['value'][2] = ' = '+ worker_id
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        db.otherDB(d.deleteSql(p))
    return 'ok'

def modify_worker(project_id, uid):
    # uid(split by ',') change to list
    # update user participate in project
    uid = uid.split(',')
    p = {}
    p['select_key'] = ['person_id']
    p['tablename'] = 'project_participant'
    p['key'] = ['project_id']
    p['value'] = [' = '+project_id]
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    A = db.selectDB(d.selectSql(p))

    only_A = []
    A_and_B = []
    only_B = []
    for record in A:
        if record['person_id'] in uid:
            A_and_B.append(record['person_id'])
        else:
            only_A.append(record['person_id'])
    only_B = list(set(uid)-set(A_and_B))
    #insert for only_B
    p.clear()
    p['tablename'] = 'project_participant'
    p['column'] = ['person_id','project_id']
    p['values'] = ['unknown',project_id,]
    for worker_id in only_B:
        p['values'][0] = worker_id
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        db.otherDB(d.insertSql(p))
    #delete for only_A
    p.clear()
    p['tablename'] = 'project_participant'
    p['key'] = ['project_id','person_id']
    p['value'] = [' = '+project_id,'unknown']
    for worker_id in only_A:
        p['value'][1] = ' = '+ worker_id
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        db.otherDB(d.deleteSql(p))
    
    return 'ok'

def get_authority(project_id, uid=None):
    if uid is not None:
        # return ( git_authority, file_authority, mail_authority)
        sql = f'''select distinct git_authority, file_authority, mail_authority from authority where project_id=\'{project_id}\' and worker_id={uid};'''
    else:
        # return (uid, name, git_authority, file_authority, mail_authority)
        sql = f'''select distinct a.worker_id, e.name, a.git_authority, a.file_authority, a.mail_authority
                  from authority as a
                  join employee as e on a.worker_id=e.id
                  where a.project_id=\'{project_id}\';'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.selectDB(sql)

def modify_authority(project_id, uid, git_authority, file_authority, mail_authority):
    # if can't find project_id uid in table, return 'error'
    sql = f'''update authority set git_authority={git_authority}, file_authority={file_authority}, mail_authority={mail_authority} where project_id=\'{project_id}\' and worker_id={uid};'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return 'ok' if db.otherDB(sql) == 'ok' else 'error'

def get_business_area():
    sql = 'select id as business_id, name as business_name from business_area where delete_label=0;'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.selectDB(sql)

if __name__ == '__main__':
    print(get_info(keyword='系统', include_reject=True))
