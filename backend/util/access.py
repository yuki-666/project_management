import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))

from flask import json, request
import config

def get_value_dict():
    ret = request.get_json()
    if ret is None:
        if request.method == 'GET':
            ret = dict(request.args)
        elif request.method == 'POST':
            ret = dict(request.form)

    for key, value in ret.items():
        if isinstance(value, list):
            ret[key] = value[0]

    return ret

def check_dict(data, keys):
    for key in keys:
        if key not in data.keys():
            return False
    
    return True

def has_error(data):
    if data == config.error_value:
        return True
    else:
        return False
