# !/usr/bin/python
# encoding=utf-8

from flask import json, Flask, request
from flask_cors import *

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

@app.route('/login', methods=['GET', 'POST'] )
def hello():
    data = get_value_dict()
    print(data)
    if request.method == 'GET':
        return '[GET METHOD] your name is ' + request.args.get('name', 'unknown')
    else:
        return '[POST METHOD] your name is '+ request.form.get('name', 'unknown')

if __name__ == '__main__':
    app.run(port=7777, debug=True, host='127.0.0.1')
