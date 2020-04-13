import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))
import config
import util.db as d
import config

def get_info_by_uid(uid, is_superior=False, include_finished=False):
    # is_superior=True: uid是上级的uid，要获取他所有项目下级的工时
    # is_superior=False: uid是自己的uid，获取自己所有工时
    # include_finished: whether return approved part

    if is_superior:
        sql = f'''
               select distinct work_time.id, employee.name as worker_name, project_function.function_name, work_time.event_name, work_time.start_time, work_time.end_time, project.name as project_name
               from work_time
               join employee on work_time.worker_id=employee.id
               join project_function on work_time.function_id=project_function.id
               join project_participant on project_participant.person_id=work_time.worker_id
               join project on project.id = work_time.project_id
               where work_time.delete_label=0 and project_participant.leader_id=\'{uid}\';'''
    else:
        sql = f'''
               select distinct work_time.id, employee.name as worker_name, project_function.function_name, work_time.event_name, work_time.start_time, work_time.end_time, work_time.status, project.name as project_name
               from work_time
               join employee on work_time.worker_id=employee.id
               join project_function on work_time.function_id=project_function.id
               join project on project.id = work_time.project_id 
               where work_time.delete_label=0 and work_time.worker_id=\'{uid}\';'''

    if not include_finished:
        sql = sql[:-1] + ' and work_time.status=1;'

    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    return res if res != 'Empty' else []

def get_info_by_work_time_id(work_time_id):
    para_dict = {}
    para_dict['select_key'] = ['work_time.id', 'employee.name', 'project_function.function_name', 'work_time.event_name', 'work_time.start_time', 'work_time.end_time','work_time.delete_label','project.name as project_name']
    para_dict['select_value'] = []
    para_dict['tablename'] = 'work_time'
    para_dict['key'] = ['work_time.id','work_time.delete_label']
    work_time_id = '=' + work_time_id
    para_dict['value'] = [work_time_id,'!=1']
    para_dict['join_tablename'] = ['employee','project_function','project']
    para_dict['on_key'] = ['employee.id','project_function.id','work_time.project_id']
    para_dict['on_value'] = ['work_time.worker_id','work_time.function_id','project.id']

    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(d.selectSql(para_dict))
    if res == 'Empty' :
        return 'error'
    return res
    # return error if delete label = 1
    # check if work_time_id exist, return 'error' if not
    
def get_info_by_uid_project_id(uid, project_id):
    sql = f'''
           select distinct work_time.id as work_time_id, project.id as project_id, project.name as project_name, project_function.function_name, work_time.event_name, work_time.start_time, work_time.end_time, work_time.date, timestampdiff(minute,work_time.start_time,work_time.end_time) as work_time, work_time.remain, work_time.status, work_time.describe
           from work_time
           join project on project.id=work_time.project_id
           join project_function on project_function.id=work_time.function_id
           where work_time.worker_id={uid} and work_time.project_id={project_id} and work_time.delete_label=0;'''

    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)

    if res == 'Empty':
        return []

    for record in res:
        record['work_time'] = record['work_time'] / 60
    return res

def confirm(work_time_id, status):
    # return 'error' if work_time_id not found
    # return error if delete label = 1
    # check if project status is 1 (pending), return 'error' if not
    # modify project status, from 1 to 0/2 (rejection/approved)

    sql = f'update work_time set status={status} where id={work_time_id} and delete_label=0 and status=1;'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.otherDB(sql)
    return res if res != 'none' else 'error'

def modify(work_time_id, event_name, start_time, end_time):
    # modify project info, search by id
    # return 'error' if work_time_id not found
    # return error if delete label = 1

    sql = f'''
           update work_time
           set event_name=\'{event_name}\', start_time=\'{start_time}\', end_time=\'{end_time}\'
           where id=\'{work_time_id}\' and delete_label=0;'''
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.otherDB(sql)
    return res if res != 'none' else 'error'

def delete(work_time_id):
    sql = f'select delete_label from work_time where id = {work_time_id};'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    if res == 'Empty': 
        # can't find work_time_id
        return 'error'
    if res[0]['delete_label'] == '1':
        # already delete
        return 'ok'

    sql = f'update work_time set delete_label = 1 where id = {work_time_id};'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.otherDB(sql)
    return res

def create(uid, project_id, date, function_id, event_name, start_time, end_time, remain, describe):
    # TODO:
    # status: "ok"/"fail_x" (fail_1: work_time > 24h, fail_2: start_time < end_time, fail_3: remain < 0)
    # 1. check fail_1, fail_2, fail_3
    # 2. get max id
    # 3. insert (status=1, delete_label=0)
    return 'ok'
