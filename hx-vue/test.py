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

@app.route(base_route + '/homepage/login', methods=['POST'])
def homepage_login():
    request_data = get_value_dict()
    print(request_data)
    
    ret = {}
    ret['status'], ret['uid'], ret['career'] = 0, 123, 0

    print(json.dumps(ret)) # {"career": 0, "status": 0, "uid": 123}
    return json.dumps(ret)

if __name__ == '__main__':
    app.run(port=7777, debug=True, host='127.0.0.1')
