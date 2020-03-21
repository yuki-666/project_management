import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..')) # backend/
import config
import util.db as d

def selectSql(p):
    sql = '''select ''' + p['select_key'][0]
    for i in range(1,len(p['select_key'])):
        sql = sql + ''', ''' + p['select_key'][i] 
    sql = sql + ''' from ''' + p['tablename'] 
    if len(p['join_tablename'])>0:
        sql = sql + ''' join ''' + p['join_tablename'][0]
        for i in range(1,len(p['join_tablename'])):
            sql = sql + ''',''' + p['join_tablename'][i] 
        if len(p['on_key'])>0:
            sql = sql + ''' on ''' + p['on_key'][0] + ''' = '''+p['on_value'][0]
            for i in range(1,len(p['on_key'])):
                sql = sql + ''' and ''' + p['on_key'][i] + ''' = '''+p['on_value'][i]
    if len(p['key'])>0:
        sql = sql + ''' where ''' + p['key'][0] + p['value'][0]
        for i in range(1,len(p['key'])):
            sql = sql + ''' and ''' + p['key'][i] + p['value'][i]
    sql = sql + ''';'''
    print(sql)#删
    return sql

def updateSql(p):
    sql = '''update ''' + p['tablename'] + ''' set ''' + p['set_key'][0] + ''' = '%s' ''' % p['set_value'][0]
    for i in range(1,len(p['set_key'])):
        sql = sql + ''' , ''' + p['set_key'][i] + ''' = '%s' ''' % p['set_value'][i]
    if len(p['where_key'])>0:
        sql = sql + ''' where ''' + p['where_key'][0] + p['where_value'][0]
        for i in range(1,len(p['where_key'])):
            sql = sql + ''' and ''' + p['where_key'][i] + p['where_value'][i]
    sql = sql + ''';'''
    print(sql)#删
    return sql


# maybe move to another place called 'project'
def modify_project(project_id, project_name,  describe,scheduled_time, delivery_day, project_superior_id, \
    major_milestones, adopting_technology, business_area, main_function):
    # modify project info, search by id
    sql = '''update project
    set name = '%s', describe = '%s' ,reserve_date = '%s',submit_date = '%s', project_leader_id = '%s',major_milestones = '%s',tech = '%s',domain_id = '%s',main_function ='%s'
    where id = '%s';''' %(project_name,  describe,scheduled_time, delivery_day, project_superior_id, \
    major_milestones, adopting_technology, business_area, main_function,project_id)
    
     #id | name  | status | customer_id | main_function 
     #| domain_id | tech   | project_leader_id | submit_date | reserve_date | update_time     

    db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
    return db.otherDB(sql)

# maybe move to another place called 'project'
def confirm_project(project_id, status):
    sql = '''update project set status = '%s' where id = '%s' and status =1;'''%(project_id,status)
    db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
    res = db.otherDB(sql)
    if res == 'ok':
        return 'ok'
    else :
        return 'error'
    # check if project status is 1 (pending), return 'error' if not
    # modify project status, from 1 to 0/2 (rejection/established)

# maybe move to another place called 'work_time'
def get_work_time_by_uid(uid, is_superior=False, include_finished=False):
    # id | worker_id | project_id | date  | event_name | remain | status | remarks |start_time|end_time
    para_dict = {}
    para_dict['select_key'] = ['work_time.id', 'employee.name', 'work_time.function_name', 'work_time.event_name', 'work_time.start_time', 'work_time.end_time']
    para_dict['select_value'] = []
    para_dict['tablename'] = 'work_time'
    para_dict['join_tablename'] = ['employee']
    para_dict['on_key'] = ['work_time.worker_id']
    para_dict['on_value'] = ['employee.id']
    para_dict['key'] = ['work_time.delete_label']
    para_dict['value'] = ['=0']
    if include_finished:
        para_dict['select_key'].append('status')
    else:
        #return unapproved part
        para_dict['key'].append('work_time.status')
        para_dict['value'].append('<2')
    if is_superior :
        para_dict['join_tablename'].append('project_participant')
        para_dict['key'].append('project_participant.leader_id')
        uid = '=' + uid
        para_dict['value'].append(uid)
        para_dict['on_key'].append('project_participant.person_id')
        para_dict['on_value'].append('work_time.worker_id')
    else :
        para_dict['key'].append('work_time.worker_id')
        uid = '=' + uid
        para_dict['value'].append(uid)
    db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
    return db.selectDB(selectSql(para_dict))
    # is_superior=True: uid是上级的uid，要获取他所有项目下级的工时
    # is_superior=False: uid是自己的uid，获取自己所有工时
    # include_finished: whether return approved part
    
# maybe move to another place called 'work_time'
def get_work_time_by_work_time_id(work_time_id):
    para_dict = {}
    para_dict['select_key'] = ['work_time.id', 'employee.name', 'work_time.function_name', 'work_time.event_name', 'work_time.start_time', 'work_time.end_time','work_time.delete_label']
    para_dict['select_value'] = []
    para_dict['tablename'] = 'work_time'
    para_dict['key'] = ['work_time.id','delete_label']
    work_time_id = '=' + work_time_id
    para_dict['value'] = [work_time_id,'!=1']
    para_dict['join_tablename'] = ['employee']
    para_dict['on_key'] = ['employee.id']
    para_dict['on_value'] = ['work_time.worker_id']

    db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
    sql = selectSql(para_dict)
    res = db.selectDB(sql)
    if res == 'Empty' :
        return 'error'
    # return error if delete label = 1
    # check if work_time_id exist, return 'error' if not
    return res
# maybe move to another place called 'work_time'
def confirm_work_time(work_time_id, status):
    para_dict = {}
    para_dict['tablename'] = 'work_time'
    para_dict['set_key'] = ['status']
    para_dict['set_value'] = [status]
    para_dict['where_key'] = ['id','delete_label','status']
    work_time_id = '=' + work_time_id
    para_dict['where_value'] = [work_time_id,'=0','=1']
    
    db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
    sql = updateSql(para_dict)
    res = db.otherDB(sql)
    if res == 'none' :
        return 'error'
    return res
    # return 'error' if work_time_id not found
    # return error if delete label = 1
    # check if project status is 1 (pending), return 'error' if not
    # modify project status, from 1 to 0/2 (rejection/approved)

# maybe move to another place called 'work_time'
def modify_word_time(work_time_id, function_name, event_name, start_time, end_time):
    para_dict = {}
    para_dict['tablename'] = 'work_time'
    para_dict['set_key'] = ['function_name', 'event_name', 'start_time', 'end_time']
    para_dict['set_value'] = [function_name, event_name, start_time, end_time]
    para_dict['where_key'] = ['id','delete_label']
    work_time_id = '=' + work_time_id
    para_dict['where_value'] = [work_time_id,'=0']

    db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
    sql = updateSql(para_dict)
    res = db.otherDB(sql)
    if res == 'none' :
        return 'error'
    return res
    # modify project info, search by id
    # return 'error' if work_time_id not found
    # return error if delete label = 1

def delete_work_time(work_time_id):
    p = {}
    p['select_key'] = ['delete_label']
    p['tablename'] = 'work_time'
    p['join_tablename'] = []
    p['on_key'] = []
    p['on_value'] = []
    p['key'] = ['id']
    work_time_id = '=' + work_time_id
    p['value'] = [work_time_id]
    db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
    sql = selectSql(p)
    res = db.selectDB(sql)
    if res == 'Empty':#id不存在
        return 'error'
    if res[0]['delete_label'] =='1':#已删除
        return 'ok'


    para_dict = {}
    para_dict['tablename'] = 'work_time'
    para_dict['set_key'] = ['delete_label']
    para_dict['set_value'] = ['1']
    para_dict['where_key'] = ['id']
    work_time_id = '=' + work_time_id
    para_dict['where_value'] = [work_time_id]

    db = d.ConnectToMysql(config.host,config.username,config.password,config.database,config.port)
    sql = updateSql(para_dict)
    return db.otherDB(sql)
    # return 'error' if work_time_id not found
    # add delete label (set delete_label column to 1, default is 0)
    

    
