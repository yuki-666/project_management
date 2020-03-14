import sys
sys.path.append('..')
import config
import numpy as np
import util.db as db

def login(username, password):
    para_dict = {}
    para_dict['select_key'] = 'id'
    para_dict['select_value'] = []
    para_dict['table_name'] = 'login'
    para_dict['key'] = ['username','password']
    para_dict['value'] = [username,password]
    status = db.select(para_dict)
    if status == 'ok':
        uid = para_dict['select_value']

    para_dict['select_key'] = 'career'
    para_dict['select_value'] = []
    para_dict['table_name'] = 'employee'
    para_dict['key'] = 'id'
    para_dict['value'] = uid
    status = db.select(para_dict)
    if status == 'ok':
        career = para_dict['select_value']
    # if ok: return uid and career, else return status
    # status: 0，1，2 ok, username_not_exist, password_error
    s['ok'] = 0
    s['username_not_exist'] = 1
    s['password_error'] = 2
    if status == 'ok':
        return (s[status],uid, career)
    else:
        return s[status]

def search(project_id, project_name):
    id, name, status = 0, 1, 2 # index in db result, need to be modify
    
    para_dict = {}
    para_dict['select_key'] = ['id','name','status']
    para_dict['select_value'] = []
    para_dict['tablename'] = 'project'
    para_dict['key'] = []
    para_dict['value'] = []

    if project_id != config.none_value:
        para_dict['key'].append('id')
        para_dict['value'].append(project_id)
    
    if project_name != config.none_value:
            
        para_dict['key'].append('name')
        para_dict['value'].append(project_name)
                
    if len(para_dict['key']) == 0 or not db.select(para_dict)=='ok':
        return 'error'

    # used for test
    # db_result = [[1, 2, 3],
    #              [4, 5, 3]]
    db_result = para_dict['select_value']
    db_result = np.array(db_result, dtype=np.str)
    return (list(db_result[:, id]), list(db_result[:, name]), list(db_result[:, status]))

def get_project(page, size, uid=None):
    # TODO
    # 1. get project from db
    # 2. sort by update_time
    # 3. return page * size ~ page * (size + 1)

    id, name, status, update_time = 0, 1, 2, 3 # index in db result, need to be modify
    para_dict = {}
    para_dict['select_value'] = []
    para_dict['table_name'] = 'project'

    if uid is None:
        para_dict['select_key'] = '*'
        pass
    else:
        para_dict['select_key'] = 'id'
        pass
    db.select(para_dict)
    # used for test
    # db_result = [[1, 2, 3, '2020-03-10'],
    #              [4, 5, 3, '2020-03-11']]

    tmp = np.array(para_dict['select_value'], dtype=np.str)
    db_result = np.array(tmp)
    l = np.argsort(tmp[:,update_time])
    for i in range(l.shape[0]):
        db_result[l.shape[0] - 1 - l[i]] = tmp[i] 
    return (list(db_result[:, id]), list(db_result[:, name]), list(db_result[:, status]), list(db_result[:, update_time]))

if __name__ == "__main__":
    tmp = np.array([[1, 2, 3, '2020-03-10'],
            [4, 5, 3, '2020-03-11']])

    db_result = np.array(tmp)
    l = np.argsort(tmp[:,3])
    
    length =  l.shape[0]
    for i in range(length):
        
        db_result[length-1-l[i]] = tmp[i]
    print(db_result)