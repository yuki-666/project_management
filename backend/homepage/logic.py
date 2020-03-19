import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..')) # backend/
import config
import util.db as d

def login(username, password):
    #login:id   | username  | password 
    #employee:id   | name      | gender | career       
    #| superior_id | tele     | department | mailbox  |
    sql = '''select login.id,employee.career
             from login join employee
             on login.id = employee.id
             where login.username = '%s' and login.password = '%s';''' %(username,password)
    
    db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
    res = db.selectDB(sql)
    
    # TODO
    # print(res)
    # print(res[0]['career'])
    if not res == 'Empty':
        if res['career'] != 'NULL':
            return (0,res)
        #leader or worker
        sql = '''select 2 from project_participant join employee
                 where employee.username = '%s' and employee.id = project_participant.leader_id;''' % username
        db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
        if db.selectDB(sql) == 'Empty':
            res['career'] = 3
            return (0,res)
        else:
            res['career'] = 2
            return (0,res)
    else :
        sql = '''select login.id,employee.career
             from login join employee
             on login.id = employee.id
             where login.username = '%s';''' % username
        db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
        res = db.selectDB(sql)
        if res == 'Empty':
            return 1
        else:
            return 2

# maybe move to another place called 'project'
def search_project(project_id=None, keyword=None, detail=False):
    #id | name            | status | customer_id | main_function
    # | domain_id | tech   | project_leader_id | submit_date | reserve_date |
    id, name, status = 0, 1, 2 # index in db result, need to be modify
    
    # if detail=False, return (id, name, status)
    # if detail=True, return (id, name, describe, scheduled_time, delivery_day, project_superior_name, major_milestones, adopting_technology, business_area, main_function)
    if detail == False:
        sql = '''select id,name,status '''
    else:
        sql = '''select id, name, describe, scheduled_time, delivery_day, project_superior_name, major_milestones, adopting_technology, business_area, main_function '''
    sql = sql + 'from project '

    # both not None
    if project_id is not None and keyword is not None:
        return 'error'

    if project_id is not None:
        sql = sql + '''where id = '%s';''' % project_id
        db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
        res = db.selectDB(sql)
        return res
    elif keyword is not None:
        # search by keyword, 在id和name模糊匹配
        like = '%'
        for i in range(len(keyword)):
            like = like + keyword[i]
            like = like + '%'
        sql_ = sql + '''where id like '%s';''' % like
        db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
        res = db.selectDB(sql_)

        if not res == 'Empty':
            return res
        sql = sql + '''where name like '%s';''' % like
        db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
        res = db.selectDB(sql)
        return res
    else:
        # both None
        return 'error'
 
# maybe move to another place called 'project'
def get_project(page, size, uid=None, include_reject=False):
    # 1. get project from db (if include_reject is True, should also include project that status is reject)
    # 2. sort by update_time
    # 3. return page * size ~ page * (size + 1)
    
    id, name, status, update_time = 0, 1, 2, 3 # index in db result, need to be modify
    sql = '''select id, name, status, update_time from project '''
    
    if not uid is None:
        sql_ = sql + '''join project_participant 
                       on project_participant.project_id = project.id 
                       where project_participant.person_id = '%s' ''' % uid
        if include_reject==False:
            sql_ = sql_ +  '''and status > 0;'''
        db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
        res = db.selectDB(sql_)
        return res

    if include_reject==False:
        sql = sql + 'where status >0;'
    print(sql)
    db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
    res = db.selectDB(sql)
    return res
    
if __name__ == "__main__":
    # TODO: fix bug.
    ret = login('卡桑', '000111')
    print(ret)
    # tmp = np.array([[1, 2, 3, '2020-03-10'],
    #         [4, 5, 3, '2020-03-11']])

    # db_result = np.array(tmp)
    # l = np.argsort(tmp[:,3])
    
    # length =  l.shape[0]
    # for i in range(length):
        
    #     db_result[length-1-l[i]] = tmp[i]
    # print(db_result)
    # p = {}
    # p['name'] = ['zs']
    # p['id'] = [0]
    # print(p)
    # like = '*'
    # keyward = 'abc'
    # for i in range(len(keyward)):
    #     like = like + keyward[i]
    #     like = like + '*'
    # print(like)
    


