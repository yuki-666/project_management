# !/usr/bin/python
# encoding=utf-8

from flask import json, Flask, request
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
base_route = '/api'

def get_value_dict():
    ret = request.get_json()
    if ret is None:
        if request.method == 'GET':
            ret = dict(request.args)
        elif request.method == 'POST':
            ret = dict(request.form)
    return ret

@app.route(base_route + '/homepage/project_mine', methods=['GET'])
def aa4():
    request_data = get_value_dict()
    print(request_data)

    ret = []
    ret.append({'id': 'hahaha', 'name': '奥凯电缆女艾斯比', 'status': '2'})
    ret.append({'id': 'hohoho', 'name': 'asegbbsdgsdgrgv', 'status': '4'})

    print(json.dumps(ret))
    return json.dumps(ret)

@app.route(base_route + '/homepage/login', methods=['POST'])
def homepage_login():
    request_data = get_value_dict()
    print(request_data)
    
    ret = {}
    ret['status'], ret['uid'], ret['career'] = 0, 123, 1

    print(json.dumps(ret)) # {"career": 0, "status": 0, "uid": 123}
    return json.dumps(ret)

@app.route(base_route + '/project_detail/function/modify', methods=['POST'])
def aaa():
    request_data = get_value_dict()
    print(request_data)
    
    ret = {}
    ret['status'], ret['uid'], ret['career'] = 0, 123, 0

    print(json.dumps(ret)) # {"career": 0, "status": 0, "uid": 123}
    return json.dumps(ret)

@app.route(base_route + '/project_detail/function', methods=['GET'])
def aa():
    request_data = get_value_dict()
    print(request_data)

    ret = []
    ret.append({'function_id': '123', 'function_name': 'fdsa', 'worker_name': '奥凯电缆女艾斯比'})
    ret.append({'function_id': '1237', 'function_name': 'fdsa', 'worker_name': 'akdlhgab'})

    print(json.dumps(ret))
    return json.dumps(ret)

@app.route(base_route + '/project_detail/project_worker', methods=['GET'])
def aa2():
    request_data = get_value_dict()
    print(request_data)

    ret = []
    ret.append({'project_name': 'hahaha', 'worker_name': '奥凯电缆女艾斯比'})
    ret.append({'project_name': 'hohoho', 'worker_name': 'akdlhgab'})

    print(json.dumps(ret))
    return json.dumps(ret)

@app.route(base_route + '/project_detail/project_worker/modify_worker/save', methods=['POST'])
def aa3():
    request_data = get_value_dict()
    print(request_data)
    
    ret = {}
    ret['status'], ret['uid'], ret['career'] = 0, 123, 0

    print(json.dumps(ret)) # {"career": 0, "status": 0, "uid": 123}
    return json.dumps(ret)

@app.route(base_route + '/project_detail/modify/show', methods=['GET'])
def ccc():
    data = {}
    data['id'] = '11'
    data['name'] = '11'
    data['project_superior_id'] = '01'
    data['update_time'] = '2020-04-18 01:16:41'
    data['describe'] = '11'
    data['scheduled_time'] = '2020-03-03 00:00:00'
    data['delivery_day'] = '2020-03-20 00:00:00'
    data['project_superior_name'] = 'gsggf'
    data['major_milestones'] = '11'
    data['adopting_technology'] = '11'
    data['business_area'] = '01'
    data['main_function'] = '11'
    data['project_superior'] = [{'project_superior_id': '01', 'project_superior_name': 'aaa'}]
    data['business'] = [{'business_id': '01', 'business_name': 'bbb'}]
    data['status'] = '5'

    print(json.dumps(data))
    return json.dumps(data)

if __name__ == '__main__':
    app.run(port=7777, debug=True, host='127.0.0.1')

