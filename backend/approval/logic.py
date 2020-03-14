import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..')) # backend/
import config
import util.db as db

# maybe move to another place called 'project'
def modify_project(project_id, project_name, describe, scheduled_time, delivery_day, project_superior_name, \
    major_milestones, adopting_technology, business_area, main_function):
    # TODO
    # modify project info, search by id
    # return 'error' if project_id not found
    return 'ok'

# maybe move to another place called 'project'
def confirm_project(project_id, status):
    # TODO
    # return 'error' if project_id not found
    # check if project status is 1 (pending), return 'error' if not
    # modify project status, from 1 to 0/2 (rejection/established)
    return 'ok'

# maybe move to another place called 'work_time'
def get_work_time_by_uid(uid, is_superior=False, include_finished=False):
    # TODO
    # not return delete label = 1
    # is_superior=True: uid是上级的uid，要获取他所有项目下级的工时
    # is_superior=False: uid是自己的uid，获取自己所有工时
    # include_finished: whether return approved part

    if include_finished:
        return (work_time_id, worker_name, function_name, event_name, start_time, end_time, status)
    else:
        return (work_time_id, worker_name, function_name, event_name, start_time, end_time)

# maybe move to another place called 'work_time'
def get_work_time_by_work_time_id(work_time_id):
    # TODO
    # return error if delete label = 1
    # check if work_time_id exist, return 'error' if not
    return (work_time_id, worker_name, function_name, event_name, start_time, end_time)

# maybe move to another place called 'work_time'
def confirm_work_time(work_time_id, status):
    # TODO
    # return 'error' if work_time_id not found
    # return error if delete label = 1
    # check if project status is 1 (pending), return 'error' if not
    # modify project status, from 1 to 0/2 (rejection/approved)
    return 'ok'

# maybe move to another place called 'work_time'
def modify_word_time(work_time_id, worker_name, function_name, event_name, start_time, end_time):
    # TODO
    # modify project info, search by id
    # return 'error' if work_time_id not found
    # return error if delete label = 1
    return 'ok'

def delete_work_time(work_time_id):
    # TODO
    # return 'error' if work_time_id not found
    # add delete label (set delete_label column to 1, default is 0)
    return 'ok'
