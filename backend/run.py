# !/usr/bin/python
# encoding=utf-8

from flask import json, Flask, request
from flask_cors import *
import homepage.logic as homepage
import approval.logic as approval

app = Flask(__name__)
CORS(app, supports_credentials=True)

def get_value_dict():
    ret = request.get_json()
    if ret is None:
        if request.method == 'GET':
            ret = dict(request.args)
        elif request.method == 'POST':
            ret = dict(request.form)
    return ret

def check_dict(data, keys):
    for key in keys:
        if key not in data.keys():
            return False
    
    return True

def has_error(data):
    if type(data) == str and data == 'error':
        return True
    else:
        return False


# homepage

@app.route('/homepage/login', methods=['POST'])
def homepage_login():
    request_data = get_value_dict()
    if not check_dict(request_data, ['username', 'password']):
        return json.dumps('PARAM ERROR')

    data = homepage.login(request_data['username'], request_data['password'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/login')
    elif type(data) == str:
        return json.dumps(data)
    else:
        ret = {}
        ret['status'], ret['uid'], ret['career'] = data
        return json.dumps(ret)

@app.route('/homepage/search', methods=['POST'])
def homepage_search():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id', 'name']):
        return json.dumps('PARAM ERROR')

    data = homepage.search_project(request_data['id'], request_data['name'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/search')
    else:
        ret = {}
        ret['id'], ret['name'], ret['status'] = data
        return json.dumps(ret)

@app.route('/homepage/project_all', methods=['GET'])
def homepage_project_all():
    request_data = get_value_dict()
    if not check_dict(request_data, ['page', 'size']):
        return json.dumps('PARAM ERROR')

    data = homepage.get_project(request_data['page'], request_data['size'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/project_all')
    else:
        ret = {}
        ret['id'], ret['name'], ret['status'], ret['update_time'] = data
        return json.dumps(ret)

@app.route('/homepage/project_mine', methods=['GET'])
def homepage_project_mine():
    request_data = get_value_dict()
    if not check_dict(request_data, ['page', 'size', 'uid']):
        return json.dumps('PARAM ERROR')

    data = homepage.get_project(request_data['page'], request_data['size'], uid=request_data['uid'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/project_mine')
    else:
        ret = {}
        ret['id'], ret['name'], ret['status'], ret['update_time'] = data
        return json.dumps(ret)


# approval

@app.route('/approval/project', methods=['GET'])
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

@app.route('/approval/project/show', methods=['GET'])
def approval_project_show():
    request_data = get_value_dict()
    if not check_dict(request_data, ['id']):
        return json.dumps('PARAM ERROR')

    data = homepage.search_project(request_data['id'], config.none_value, detail=True)

    if has_error(data):
        return json.dumps('ERROR route:/approval/project/show')
    else:
        ret = {}
        ret['id'], ret['name'], ret['describe'], ret['scheduled_time'], ret['delivery_day'], \
            ret['project_superior_name'], ret['major_milestones'], ret['adopting_technology'], \
            ret['business_area'], ret['main_function'] = data
        return json.dumps(ret)

@app.route('/approval/project/modify', methods=['POST'])
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

@app.route('/approval/project/confirm', methods=['POST'])
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

@app.route('/approval/work_time/initiative', methods=['GET'])
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

@app.route('/approval/work_time/confirm', methods=['POST'])
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

@app.route('/approval/work_time/initiative/show', methods=['GET'])
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

@app.route('/approval/work_time/passive', methods=['GET'])
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

@app.route('/approval/work_time/passive/show', methods=['GET'])
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

@app.route('/approval/work_time/passive/modify', methods=['POST'])
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

@app.route('/approval/work_time/passive/delete', methods=['POST'])
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

if __name__ == '__main__':
    app.run(port=7777, debug=True, host='127.0.0.1')
