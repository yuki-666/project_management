import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))
import util.db as d
import config

def get_info_by_uid(uid, is_superior=False, include_finished=False):
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
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.selectDB(d.selectSql(para_dict))
    # is_superior=True: uid是上级的uid，要获取他所有项目下级的工时
    # is_superior=False: uid是自己的uid，获取自己所有工时
    # include_finished: whether return approved part

def get_info_by_work_time_id(work_time_id):
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

    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(d.selectSql(para_dict))
    if res == 'Empty' :
        return 'error'
    return res
    # return error if delete label = 1
    # check if work_time_id exist, return 'error' if not
    
def get_info_by_uid_project_id(uid, project_id):
    para_dict = {}
    para_dict['select_key'] = ['work_time.id', 'project.name', 'project_function.function_name', 'work_time.event_name',\
     'work_time.start_time', 'work_time.end_time','work_time.date','timestampdiff(minute,work_time.start_time,work_time.end_time)','work_time.remain','work_time.status','work_time.describe']
    para_dict['tablename'] = 'work_time'
    para_dict['join_tablename'] = ['project,project_function']
    para_dict['on_key'] = ['project.id','project_function.id']
    para_dict['on_value'] = ['work_time.project_id','work_time.function_id']
    para_dict['key'] = ['work_time.worker_id','work_time.project_id']
    para_dict['value'] = [' = '+uid,' = '+project_id]
    
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(d.selectSql(para_dict))
    # return (work_time_id, project_name, function_name, activity_name, start_time, end_time, date, work_time, remain, status, describe)
    

def confirm(work_time_id, status):
    para_dict = {}
    para_dict['tablename'] = 'work_time'
    para_dict['set_key'] = ['status']
    para_dict['set_value'] = [status]
    para_dict['where_key'] = ['id','delete_label','status']
    work_time_id = '=' + work_time_id
    para_dict['where_value'] = [work_time_id,'=0','=1']
    
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.otherDB(d.updateSql(para_dict))
    if res == 'none' :
        return 'error'
    return res
    # return 'error' if work_time_id not found
    # return error if delete label = 1
    # check if project status is 1 (pending), return 'error' if not
    # modify project status, from 1 to 0/2 (rejection/approved)

def modify(work_time_id, function_name, event_name, start_time, end_time):
    para_dict = {}
    para_dict['tablename'] = 'work_time'
    para_dict['set_key'] = ['function_name', 'event_name', 'start_time', 'end_time']
    para_dict['set_value'] = [function_name, event_name, start_time, end_time]
    para_dict['where_key'] = ['id','delete_label']
    work_time_id = '=' + work_time_id
    para_dict['where_value'] = [work_time_id,'=0']

    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.otherDB(d.updateSql(para_dict))
    if res == 'none' :
        return 'error'
    return res
    # modify project info, search by id
    # return 'error' if work_time_id not found
    # return error if delete label = 1

def delete(work_time_id):
    p = {}
    p['select_key'] = ['delete_label']
    p['tablename'] = 'work_time'
    p['join_tablename'] = []
    p['on_key'] = []
    p['on_value'] = []
    p['key'] = ['id']
    work_time_id = '=' + work_time_id
    p['value'] = [work_time_id]
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(d.selectSql(p))
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

    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.otherDB(d.updateSql(para_dict))
    # return 'error' if work_time_id not found
    # add delete label (set delete_label column to 1, default is 0)
