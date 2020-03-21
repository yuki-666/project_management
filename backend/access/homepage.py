import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))

from flask import json, Blueprint
from logic import login, project
from util.access import *

homepage_access = Blueprint('homepage_access', __name__)

@homepage_access.route('/login', methods=['POST'])
def login():
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
            return json.dumps(ret)

@homepage_access.route('/search', methods=['POST'])
def search():
    request_data = get_value_dict()
    if not check_dict(request_data, ['keyword']):
        return json.dumps('PARAM ERROR')

    data = project.get_project(keyword=request_data['keyword'])
    data = [i['id'] for i in data]

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@homepage_access.route('/project_all', methods=['GET'])
def project_all():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid']):
        return json.dumps('PARAM ERROR')

    data = project.get_project()

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@homepage_access.route('/project_mine', methods=['GET'])
def project_mine():
    request_data = get_value_dict()
    if not check_dict(request_data, ['uid']):
        return json.dumps('PARAM ERROR')

    data = project.get_project(uid=request_data['uid'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)
