import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))

from flask import json, Blueprint
from util.access import *
import approval.logic as logic

approval_access = Blueprint('approval_access', __name__)

@approval_access.route('/project', methods=['GET'])
def approval_project():
    request_data = get_value_dict()
    if not check_dict(request_data, ['page', 'size', 'uid']):
        return json.dumps('PARAM ERROR')
    
    data = homepage.get_project(request_data['page'], request_data['size'], uid=request_data['uid'], include_reject=True)

    if has_error(data):
        return json.dumps('ERROR route:/approval/project')
    else:
        ret = {}
        ret['id'], ret['name'], ret['status'], ret['update_time'] = data
        return json.dumps(ret)

@approval_access.route('/project/show', methods=['GET'])
def approval_project_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')

    data = homepage.search_project(project_id=request_data['id'], detail=True)

    if has_error(data):
        return json.dumps('ERROR route:/approval/project/show')
    else:
        ret = {}
        ret['id'], ret['name'], ret['describe'], ret['scheduled_time'], ret['delivery_day'], \
            ret['project_superior_name'], ret['major_milestones'], ret['adopting_technology'], \
            ret['business_area'], ret['main_function'] = data
        return json.dumps(ret)

@approval_access.route('/project/modify', methods=['POST'])
def approval_project_modify():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'name', 'describe', 'scheduled_time', 'delivery_day', \
        'project_superior_name', 'major_milestones', 'adopting_technology', 'business_area', 'main_function']):
        return json.dumps('PARAM ERROR')

    data = approval.modify_project(request_data['id'], request_data['name'], request_data['describe'], \
        request_data['scheduled_time'], request_data['delivery_day'], request_data['project_superior_name'], \
        request_data['major_milestones'], request_data['adopting_technology'], request_data['business_area'], request_data['main_function'])

    if has_error(data):
        return json.dumps('ERROR route:/approval/project/modify')
    else:
        ret = {}
        ret['status'] = data
        return json.dumps(ret)

@approval_access.route('/project/confirm', methods=['POST'])
def approval_project_confirm():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'status']):
        return json.dumps('PARAM ERROR')

    data = approval.confirm_project(request_data['id'], request_data['status'])

    if has_error(data):
        return json.dumps('ERROR route:/approval/project/confirm')
    else:
        ret = {}
        ret['status'] = data
        return json.dumps(ret)

@approval_access.route('/work_time/initiative', methods=['GET'])
def approval_work_time_initiative():
    request_data = get_value_dict()

    if not check_dict(request_data, ['uid']):
        return json.dumps('PARAM ERROR')

    data = approval.get_work_time_by_uid(request_data['uid'], is_superior=True)

    if has_error(data):
        return json.dumps('ERROR route:/approval/work_time/initiative')
    else:
        ret = {}
        ret['id'], ret['worker_name'], ret['function_name'], ret['event_name'], \
            ret['start_time'], ret['end_time'] = data
        return json.dumps(ret)

@approval_access.route('/work_time/confirm', methods=['POST'])
def approval_work_time_confirm():
    request_data = get_value_dict()

    if not check_dict(request_data, ['id', 'status']):
        return json.dumps('PARAM ERROR')

    data = approval.confirm_work_time(request_data['id'], request_data['status'])

    if has_error(data):
        return json.dumps('ERROR route:/approval/work_time/confirm')
    else:
        ret = {}
        ret['status'] = data
        return json.dumps(ret)

@approval_access.route('/work_time/initiative/show', methods=['GET'])
def approval_work_time_initiative_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')
    
    data = approval.get_work_time_by_work_time_id(request_data['id'])

    if has_error(data):
        return json.dumps('ERROR route:/approval/work_time/initiative/show')
    else:
        ret = {}
        ret['id'], ret['worker_name'], ret['function_name'], ret['event_name'], \
            ret['start_time'], ret['end_time'] = data
        return json.dumps(ret)

@approval_access.route('/work_time/passive', methods=['GET'])
def approval_work_time_passive():
    request_data = get_value_dict()

    if not check_dict(request_data, ['uid']):
        return json.dumps('PARAM ERROR')

    data = approval.get_work_time_by_uid(request_data['uid'], include_finished=True)

    if has_error(data):
        return json.dumps('ERROR route:/approval/work_time/passive')
    else:
        ret = {}
        ret['id'], ret['worker_name'], ret['function_name'], ret['event_name'], \
            ret['start_time'], ret['end_time'], ret['status'] = data
        return json.dumps(ret)

@approval_access.route('/work_time/passive/show', methods=['GET'])
def approval_work_time_passive_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')
    
    data = approval.get_work_time_by_work_time_id(request_data['id'])

    if has_error(data):
        return json.dumps('ERROR route:/approval/work_time/passive/show')
    else:
        ret = {}
        ret['id'], ret['worker_name'], ret['function_name'], ret['event_name'], \
            ret['start_time'], ret['end_time'] = data
        return json.dumps(ret)

@approval_access.route('/work_time/passive/modify', methods=['POST'])
def approval_work_time_passive_modify():
    request_data = get_value_dict()

    if not check_dict(request_data, ['id', 'worker_name', 'function_name', \
        'event_name', 'start_time', 'end_time']):
        return json.dumps('PARAM ERROR')

    data = approval.modify_work_time(request_data['id'], request_data['worker_name'], \
        request_data['function_name'], request_data['event_name'], request_data['start_time'], request_data['end_time'])

    if has_error(data):
        return json.dumps('ERROR route:/approval/work_time/passive/modify')
    else:
        ret = {}
        ret['status'] = data
        return json.dumps(ret)

@approval_access.route('/work_time/passive/delete', methods=['POST'])
def approval_work_time_passive_delete():
    request_data = get_value_dict()

    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')

    data = approval.delete_work_time(request_data['id'])

    if has_error(data):
        return json.dumps('ERROR route:/approval/work_time/passive/delete')
    else:
        ret = {}
        ret['status'] = data
        return json.dumps(ret)
