import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))

from flask import json, Blueprint
from util.access import *
import homepage.logic as logic

homepage_access = Blueprint('homepage_access', __name__)

@homepage_access.route('/login', methods=['POST'])
def homepage_login():
    request_data = get_value_dict()
    if not check_dict(request_data, ['username', 'password']):
        return json.dumps('PARAM ERROR')

    data = logic.login(request_data['username'], request_data['password'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/login')
    elif type(data) == int:
        return json.dumps(data)
    else:
        ret = {}
        ret['status'], ret['uid'], ret['career'] = data
        return json.dumps(ret)

@homepage_access.route('/search', methods=['POST'])
def homepage_search():
    request_data = get_value_dict()
    if not check_dict(request_data, ['keyword']):
        return json.dumps('PARAM ERROR')

    data = logic.search_project(keyword=request_data['keyword'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/search')
    else:
        ret = {}
        ret['id'], ret['name'], ret['status'] = data
        return json.dumps(ret)

@homepage_access.route('/project_all', methods=['GET'])
def homepage_project_all():
    request_data = get_value_dict()
    if not check_dict(request_data, ['page', 'size']):
        return json.dumps('PARAM ERROR')

    data = logic.get_project(request_data['page'], request_data['size'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/project_all')
    else:
        ret = {}
        ret['id'], ret['name'], ret['status'], ret['update_time'] = data
        return json.dumps(ret)

@homepage_access.route('/project_mine', methods=['GET'])
def homepage_project_mine():
    request_data = get_value_dict()
    if not check_dict(request_data, ['page', 'size', 'uid']):
        return json.dumps('PARAM ERROR')

    data = logic.get_project(request_data['page'], request_data['size'], uid=request_data['uid'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/project_mine')
    else:
        ret = {}
        ret['id'], ret['name'], ret['status'], ret['update_time'] = data
        return json.dumps(ret)
