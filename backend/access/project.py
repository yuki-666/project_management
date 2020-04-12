import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))

from flask import json, Blueprint
from logic import project, user, work_time
from util.access import *
import config

project_access = Blueprint('project_access', __name__)

@project_access.route('/mine', methods=['GET'])
def project_mine():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid', 'career']):
        return json.dumps('PARAM ERROR')

    if int(request_data['career']) == config.career_project_manager:
        data = project.get_info(uid=request_data['uid'], include_reject=True)
    else:
        data = project.get_info_include_work_time(request_data['uid'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@project_access.route('/modify/show', methods=['GET'])
def project_modify_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['project_id']):
        return json.dumps('PARAM ERROR')

    data = project.get_info(project_id=request_data['project_id'], detail=True, include_reject=True)[0]
    data_project_superior = user.get_project_superior()
    data_business = project.get_business_area()

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        data['project_superior'] = data_project_superior
        data['business'] = data_business
        return json.dumps(data)

@project_access.route('/modify/save', methods=['POST'])
def project_modify_save():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'name', 'describe', 'scheduled_time', 'delivery_day', \
                                     'project_superior_id', 'major_milestones', 'adopting_technology', \
                                     'business_area', 'main_function']):
        return json.dumps('PARAM ERROR')
    
    data = project.modify(request_data['id'], request_data['name'], request_data['describe'], \
        request_data['scheduled_time'], request_data['delivery_day'], request_data['project_superior_id'], \
        request_data['major_milestones'], request_data['adopting_technology'], request_data['business_area'], request_data['main_function'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@project_access.route('/create/show', methods=['GET'])
def project_create_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid']):
        return json.dumps('PARAM ERROR')

    data_project_superior = user.get_project_superior()
    data_custom = user.get_custom()
    data_business = project.get_business_area()

    if has_error(data_project_superior) or has_error(data_custom):
        return json.dumps('BACKEND ERROR')
    else:
        data = {}
        data['project_superior'] = data_project_superior
        data['custom'] = data_custom
        data['business'] = data_business
        return json.dumps(data)

@project_access.route('/create/save', methods=['POST'])
def project_create_save():
    request_data = get_value_dict()
    if not check_dict(request_data, ['name', 'describe', 'development_type', 'scheduled_time', 'delivery_day', \
                                     'project_superior_id', 'custom_id', 'major_milestones', 'adopting_technology', \
                                     'business_area', 'main_function']):
        return json.dumps('PARAM ERROR')

    data = project.create(request_data['name'], request_data['describe'], request_data['development_type'], \
        request_data['scheduled_time'], request_data['delivery_day'], request_data['project_superior_id'], request_data['custom_id'], \
        request_data['major_milestones'], request_data['adopting_technology'], request_data['business_area'], request_data['main_function'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@project_access.route('/work_time', methods=['GET'])
def project_work_time():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid', 'project_id']):
        return json.dumps('PARAM ERROR')

    data = work_time.get_info_by_uid_project_id(request_data['uid'], request_data['project_id'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@project_access.route('/work_time/create/show', methods=['GET'])
def project_work_time_create_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid', 'project_id']):
        return json.dumps('PARAM ERROR')

    data = project.get_function(request_data['project_id'], worker_id=request_data['uid'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@project_access.route('/work_time/create/save', methods=['POST'])
def project_work_time_create_save():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid', 'project_id', 'date', 'function_id', 'event_name', \
                                     'start_time', 'end_time', 'remain', 'describe']):
        return json.dumps('PARAM ERROR')

    data = work_time.create(request_data['uid'], request_data['project_id'], request_data['date'], \
        request_data['function_id'], request_data['event_name'], request_data['start_time'], request_data['end_time'], \
        request_data['remain'], request_data['describe'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})
