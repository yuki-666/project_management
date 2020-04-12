import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))

from flask import json, Blueprint
from logic import project, user, work_time
from util.access import *
import config

approval_access = Blueprint('approval_access', __name__)

@approval_access.route('/project', methods=['GET'])
def approval_project():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid', 'career']):
        return json.dumps('PARAM ERROR')

    if int(request_data['career']) == config.career_project_superior:
        data = project.get_info()
        data = [i for i in data if i['status'] == 1]
    elif int(request_data['career']) == config.career_project_manager:
        data = project.get_info(uid=request_data['uid'], include_reject=True)
    else:
        if int(request_data['career']) != config.career_project_leader and int(request_data['career']) != config.career_worker:
            return json.dumps('PARAM ERROR')
        else:
            data = project.get_info(uid=request_data['uid'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@approval_access.route('/project/show', methods=['GET'])
def approval_project_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')

    data_project = project.get_info(project_id=request_data['id'], detail=True, include_reject=True)[0]
    data_project_superior = user.get_project_superior()
    data_project.pop('project_superior_name')

    if has_error(data_project) or has_error(data_project_superior):
        return json.dumps('BACKEND ERROR')
    else:
        data = data_project
        data['project_superior'] = data_project_superior
        return json.dumps(data)

@approval_access.route('/project/modify', methods=['POST'])
def approval_project_modify():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'name', 'describe', 'scheduled_time', 'delivery_day', \
        'project_superior_id', 'major_milestones', 'adopting_technology', 'business_area', 'main_function']):
        return json.dumps('PARAM ERROR')

    data = project.modify(request_data['id'], request_data['name'], request_data['describe'], \
        request_data['scheduled_time'], request_data['delivery_day'], request_data['project_superior_id'], \
        request_data['major_milestones'], request_data['adopting_technology'], request_data['business_area'], request_data['main_function'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@approval_access.route('/project/confirm', methods=['POST'])
def approval_project_confirm():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'status']):
        return json.dumps('PARAM ERROR')

    data = project.confirm(request_data['id'], request_data['status'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@approval_access.route('/project/repush', methods=['POST'])
def approval_project_repush():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')

    data = project.repush(request_data['id'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@approval_access.route('/work_time/initiative', methods=['GET'])
def approval_work_time_initiative():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid']):
        return json.dumps('PARAM ERROR')

    data = work_time.get_info_by_uid(request_data['uid'], is_superior=True)

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@approval_access.route('/work_time/confirm', methods=['POST'])
def approval_work_time_confirm():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'status']):
        return json.dumps('PARAM ERROR')

    data = work_time.confirm(request_data['id'], request_data['status'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@approval_access.route('/work_time/initiative/show', methods=['GET'])
def approval_work_time_initiative_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')
    
    data = work_time.get_info_by_work_time_id(request_data['id'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@approval_access.route('/work_time/passive', methods=['GET'])
def approval_work_time_passive():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid']):
        return json.dumps('PARAM ERROR')

    data = work_time.get_info_by_uid(request_data['uid'], include_finished=True)

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@approval_access.route('/work_time/passive/show', methods=['GET'])
def approval_work_time_passive_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')
    
    data = work_time.get_info_by_work_time_id(request_data['id'])[0]

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@approval_access.route('/work_time/passive/modify', methods=['POST'])
def approval_work_time_passive_modify():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'event_name', 'start_time', 'end_time']):
        return json.dumps('PARAM ERROR')

    data = work_time.modify(request_data['id'], request_data['event_name'], request_data['start_time'], request_data['end_time'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@approval_access.route('/work_time/passive/delete', methods=['POST'])
def approval_work_time_passive_delete():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')

    data = work_time.delete(request_data['id'])
    
    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})
