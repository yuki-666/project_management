import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))

from flask import json, Blueprint
from logic import project, user, work_time
from util.access import *
import config

project_detail_access = Blueprint('project_detail_access', __name__)

@project_detail_access.route('/info', methods=['GET'])
def project_detail_info():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')

    data = project.get_info(project_id=request_data['id'], detail=True, include_reject=True)
    business = project.get_business_area()
    for line in business:
        if data[0]['business_area'] == line['business_id']:
            data[0]['business_area'] = line['business_name']
            break

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@project_detail_access.route('/modify/show', methods=['GET'])
def project_detail_modify_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')

    data = project.get_info(project_id=request_data['id'], detail=True, include_reject=True)[0]
    data_project_superior = user.get_project_superior()
    data_business = project.get_business_area()

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        data['project_superior'] = data_project_superior
        data['business'] = data_business
        data['status'] = str(data['status'])
        return json.dumps(data)

@project_detail_access.route('/modify/save', methods=['POST'])
def project_detail_modify_save():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'name', 'describe', 'status', 'scheduled_time', 'delivery_day', \
                                     'project_superior_id', 'major_milestones', 'adopting_technology', \
                                     'business_area', 'main_function']):
        return json.dumps('PARAM ERROR')
    
    data = project.modify(request_data['id'], request_data['name'], request_data['describe'], request_data['status'], \
        request_data['scheduled_time'], request_data['delivery_day'], request_data['project_superior_id'], \
        request_data['major_milestones'], request_data['adopting_technology'], request_data['business_area'], request_data['main_function'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@project_detail_access.route('/function', methods=['GET'])
def project_detail_function():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')
    
    data = project.get_function(request_data['id'])
    
    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@project_detail_access.route('/function/get_children', methods=['GET'])
def project_detail_function_get_children():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'parent_function_id']):
        return json.dumps('PARAM ERROR')
    
    data = project.get_children_function(request_data['id'], request_data['parent_function_id'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@project_detail_access.route('/function/add', methods=['POST'])
def project_detail_function_add():
    request_data = get_value_dict()
    if not check_dict(request_data, ['project_id', 'parent_function_id', 'function_name']):
        return json.dumps('PARAM ERROR')
    
    data = project.add_function(request_data['project_id'], request_data['parent_function_id'], request_data['function_name'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@project_detail_access.route('/function/delete', methods=['POST'])
def project_detail_function_delete():
    request_data = get_value_dict()
    if not check_dict(request_data, ['project_id', 'function_id']):
        return json.dumps('PARAM ERROR')
    
    data = project.delete_function(request_data['project_id'], request_data['function_id'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@project_detail_access.route('/function/show', methods=['GET'])
def project_detail_function_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'function_id']):
        return json.dumps('PARAM ERROR')
    
    data = project.get_project_member(request_data['id'], function_id=request_data['function_id'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@project_detail_access.route('/function/modify', methods=['POST'])
def project_detail_function_modify():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'function_id', 'function_name', 'uid']):
        return json.dumps('PARAM ERROR')
    
    data = project.modify_function(request_data['id'], request_data['function_id'], request_data['function_name'], request_data['uid'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@project_detail_access.route('/project_worker', methods=['GET'])
def project_detail_project_worker():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')
    
    data = project.get_project_member(request_data['id'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@project_detail_access.route('/project_worker/add/show', methods=['GET'])
def project_detail_project_worker_add_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['project_id']):
        return json.dumps('PARAM ERROR')
    
    project_member = project.get_project_member(request_data['project_id'])
    project_member.insert(0, {'worker_id': '0000', 'worker_name': '无项目领导'})
    total_member = user.get_total_user(project_id=request_data['project_id'])

    total_member_exclude_in = []
    for i in total_member:
        if i['status'] == 0:
            total_member_exclude_in.append(i)

    if has_error(project_member) or has_error(total_member_exclude_in):
        return json.dumps('BACKEND ERROR')
    else:
        data = {}
        data['project_member'] = project_member
        data['total_member'] = total_member_exclude_in
        return json.dumps(data)

@project_detail_access.route('/project_worker/add', methods=['POST'])
def project_detail_project_worker_add():
    request_data = get_value_dict()
    if not check_dict(request_data, ['project_id', 'worker_id', 'leader_id']):
        return json.dumps('PARAM ERROR')
    
    data = project.add_project_member(request_data['project_id'], request_data['worker_id'], request_data['leader_id'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@project_detail_access.route('/project_worker/delete', methods=['POST'])
def project_detail_project_worker_delete():
    request_data = get_value_dict()
    if not check_dict(request_data, ['project_id', 'worker_id']):
        return json.dumps('PARAM ERROR')

    data = project.delete_project_member(request_data['project_id'], request_data['worker_id'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@project_detail_access.route('/authority', methods=['GET'])
def project_detail_authority():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid', 'project_id']):
        return json.dumps('PARAM ERROR')
    
    data = project.get_authority(request_data['project_id'], uid=request_data['uid'])
    for key, value in data[0].items():
        if value == 0:
            data[0][key] = '否'
        else:
            if value != 1:
                return json.dumps('BACKEND ERROR')
            data[0][key] = '是'

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@project_detail_access.route('/authority_manage', methods=['GET'])
def project_detail_authority_manage():
    request_data = get_value_dict()
    if not check_dict(request_data, ['project_id']):
        return json.dumps('PARAM ERROR')
    
    data = project.get_authority(request_data['project_id'])
    for i in range(len(data)):
        for key in ['git_authority', 'file_authority', 'mail_authority']:
            if data[i][key] == 0:
                data[i][key] = '否'
            else:
                if data[i][key] != 1:
                    return json.dumps('BACKEND ERROR')
                data[i][key] = '是'

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@project_detail_access.route('/authority_manage/modify', methods=['POST'])
def project_detail_authority_manage_modify():
    request_data = get_value_dict()
    if not check_dict(request_data, ['project_id', 'uid', 'git_authority', 'file_authority', 'mail_authority']):
        return json.dumps('PARAM ERROR')
    
    for key in ['git_authority', 'file_authority', 'mail_authority']:
        if request_data[key] == '否':
            request_data[key] = 0
        else:
            if request_data[key] != '是':
                return json.dumps({'status': 'AUTHORITY_PARAM_ERROR'})
            request_data[key] = 1

    data = project.modify_authority(request_data['project_id'], request_data['uid'], request_data['git_authority'], request_data['file_authority'], request_data['mail_authority'])
    
    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})
