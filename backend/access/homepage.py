import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))

from flask import json, Blueprint
from logic import login, project
from util.access import *

homepage_access = Blueprint('homepage_access', __name__)

@homepage_access.route('/login', methods=['POST'])
def homepage_login():
    request_data = get_value_dict()
    if not check_dict(request_data, ['username', 'password']):
        return json.dumps('PARAM ERROR')

    data = login.login(request_data['username'], request_data['password'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        if type(data) == int:
            return json.dumps({'status': data})
        else:
            status, ret = data

            ret['status'] = status
            ret['uid'] = ret['id']
            ret.pop('id')

            return json.dumps(ret)

@homepage_access.route('/search', methods=['POST'])
def homepage_search():
    request_data = get_value_dict()
    if not check_dict(request_data, ['keyword']):
        return json.dumps('PARAM ERROR')

    data = project.get_info(keyword=request_data['keyword'])
    data = [{'id': i['id']} for i in data]

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@homepage_access.route('/project_all', methods=['GET'])
def homepage_project_all():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid']):
        return json.dumps('PARAM ERROR')

    data = project.get_info()

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@homepage_access.route('/project_mine', methods=['GET'])
def homepage_project_mine():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid']):
        return json.dumps('PARAM ERROR')

    data = project.get_info(uid=request_data['uid'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)
