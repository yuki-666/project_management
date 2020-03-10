# !/usr/bin/python
# encoding=utf-8

from flask import json, Flask, request
from flask_cors import *
import homepage.logic as homepage_logic

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

def has_error(data):
    if type(data) == str and data == 'error':
        return True
    else:
        return False

@app.route('/homepage/login', methods=['POST'] )
def homepage_login():
    request_data = get_value_dict()

    data = homepage_logic.login(request_data['username'], request_data['password'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/login')
    elif type(data) == str:
        return json.dumps(data)
    else:
        ret = {}
        ret['uid'], ret['career'] = data
        return json.dumps(ret)

@app.route('/homepage/search', methods=['POST'] )
def homepage_search():
    request_data = get_value_dict()

    data = homepage_logic.search(request_data['id'], request_data['name'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/search')
    else:
        ret = {}
        ret['id'], ret['name'], ret['status'] = data
        return json.dumps(ret)

@app.route('/homepage/project_all', methods=['GET'] )
def homepage_project_all():
    request_data = get_value_dict()

    data = homepage_logic.get_project(request_data['page'], request_data['size'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/project_all')
    else:
        ret = {}
        ret['id'], ret['name'], ret['status'], ret['update_time'] = data
        return json.dumps(ret)

@app.route('/homepage/project_mine', methods=['GET'] )
def homepage_project_mine():
    request_data = get_value_dict()

    data = homepage_logic.get_project(request_data['page'], request_data['size'], uid=request_data['uid'])

    if has_error(data):
        return json.dumps('ERROR route:/homepage/project_mine')
    else:
        ret = {}
        ret['id'], ret['name'], ret['status'], ret['update_time'] = data
        return json.dumps(ret)

if __name__ == '__main__':
    app.run(port=7777, debug=True, host='127.0.0.1')
