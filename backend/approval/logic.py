import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..')) # backend/
import config
import util.db as db

# maybe move to another place called 'project'
def modify_project(project_id, project_name, describe, scheduled_time, delivery_day, project_superior_name, \
    major_milestones, adopting_technology, business_area, main_function):
    
    # modify project info, search by id
    para_dict['tablename'] = 'project'
    #id,name,status,customer_id,main_function,domain_id,tech,project_leader_id,submit_date,reserve_date

    para_dict['set_key'] = ['project_name','describe','scheduled_time','submit_date','project_leader',\
        'major_milestones','tech','domain_id','main_function']
    para_dict['set_value'] = [project_name, describe, scheduled_time, delivery_day, project_superior_name, \
    major_milestones, adopting_technology, business_area, main_function]
    para_dict['where_key'] = ['peoject_id']
    para_dict['where_value'] = [project_id]

    status = db.update(para_dict)
    return status

# maybe move to another place called 'project'
def confirm_project(project_id, status):
    para_dict['tablename'] = 'project'
    para_dict['set_key'] = ['status']
    para_dict['set_value'] = [status]
    para_dict['where_key'] = ['peoject_id','status']
    para_dict['where_value'] = [project_id,1]
    
    # check if project status is 1 (pending), return 'error' if not
    # modify project status, from 1 to 0/2 (rejection/established)
    return db.update(para_dict)

# maybe move to another place called 'work_time'
def get_work_time_by_uid(uid, is_superior=False, include_finished=False):
    para_dict['select_key'] = ['work_time_id', 'employer.name', 'function_name', 'work_time.event_name', 'work_time.start_time', 'work_time.end_time']
    para_dict['select_value'] = []
    para_dict['tablename'] = 'work_time'
    para_dict['join_tablename'] = ['employer']
    para_dict['key'] = ['delete_label','work_time.worker_id']
    para_dict['value'] = [0,'employer.id']
    if include_finished:
        para_dict['select_key'].append('status')
    if is_superior :
        para_dict['join_tablename'].append['project_participant']
        para_dict['key'].append('project_participant.leader_id')
        para_dict['value'].append(uid)
        para_dict['key'].append('project_participant.person_id')
        para_dict['value'].append('work_time.worker_id')
    else :
        para_dict['key'].append('work_time.worker_id')
        para_dict['value'].append(uid)
    db.select(para_dict)
    # is_superior=True: uid是上级的uid，要获取他所有项目下级的工时
    # is_superior=False: uid是自己的uid，获取自己所有工时
    # include_finished: whether return approved part
    result = np.array(para_dict['select_value'],dtype=np.str)
    if include_finished:
        return (list(result[:,0]),list(result[:,1]) , list(result[:,2]), list(result[:,3]), list(result[:,4]), list(result[:,5]), list(result[:,6]))
    else:
        return (list(result[:,0]),list(result[:,1]) , list(result[:,2]), list(result[:,3]), list(result[:,4]), list(result[:,5]))
    
# maybe move to another place called 'work_time'
def get_work_time_by_work_time_id(work_time_id):
    para_dict['select_key'] = ['work_time_id', 'worker_name', 'function_name', 'event_name', 'start_time', 'end_time','delete_label']
    para_dict['select_value'] = []
    para_dict['tablename'] = 'work_time'
    para_dict['key'] = ['work_time_id']
    para_dict['value'] = [work_time_id]
    status = db.select(para_dict)
    delete_label = para_dict['select_value'].pop()
    if status == 'error' or delete_label == 1 :
        return 'error'
    # return error if delete label = 1
    # check if work_time_id exist, return 'error' if not
    return tuple(para_dict['select_value'])
# maybe move to another place called 'work_time'
def confirm_work_time(work_time_id, status):
    para_dict['tablename'] = 'work_time'
    para_dict['set_key'] = ['status']
    para_dict['set_value'] = [status]
    para_dict['where_key'] = ['peoject_id','delete_label','status']
    para_dict['where_value'] = [project_id,0,1]
    status = db.update(para_dict)
    # return 'error' if work_time_id not found
    # return error if delete label = 1
    # check if project status is 1 (pending), return 'error' if not
    # modify project status, from 1 to 0/2 (rejection/approved)
    return status

# maybe move to another place called 'work_time'
def modify_word_time(work_time_id, worker_name, function_name, event_name, start_time, end_time):
    para_dict['tablename'] = 'work_time'
    para_dict['set_key'] = ['worker_name', 'function_name', 'event_name', 'start_time', 'end_time']
    para_dict['set_value'] = [worker_name, function_name, event_name, start_time, end_time]
    para_dict['where_key'] = ['work_time_id','delete_label']
    para_dict['where_value'] = [work_time_id,0]
    # modify project info, search by id
    # return 'error' if work_time_id not found
    # return error if delete label = 1
    return db.update(para_dict)

def delete_work_time(work_time_id):
    para_dict['tablename'] = 'work_time'
    para_dict['set_key'] = ['delete_label']
    para_dict['set_value'] = [1]
    para_dict['where_key'] = ['work_time_id']
    para_dict['where_value'] = [work_time_id]
    # return 'error' if work_time_id not found
    # add delete label (set delete_label column to 1, default is 0)
    return db.update(para_dict)
