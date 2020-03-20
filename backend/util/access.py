from flask import json, request

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
