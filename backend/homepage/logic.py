import config
import numpy as np

def login(username, password):
    # TODO
    # if ok: return uid and career, else return status
    # status: ok, username_not_exist, password_error
    if status == 'ok':
        return (uid, career)
    else:
        return status

def search(project_id, project_name):
    id, name, status = 0, 1, 2 # index in db result, need to be modify

    if project_id != config.none_value:
        # TODO
        if project_name != config.none_value:
            # search with both id and name, maybe empty
            pass
        else:
            # search only with id
            pass
    elif project_name != config.none_value:
        # TODO
        # search by name, maybe multiple
        pass
    else:
        return 'error'

    # used for test
    # db_result = [[1, 2, 3],
    #              [4, 5, 3]]

    db_result = np.array(db_result, dtype=np.str)
    return (list(db_result[:, id]), list(db_result[:, name]), list(db_result[:, status]))

def get_project(page, size, uid=None):
    # TODO
    # 1. get project from db
    # 2. sort by update_time
    # 3. return page * size ~ page * (size + 1)

    id, name, status, update_time = 0, 1, 2, 3 # index in db result, need to be modify
    if uid is None:
        # get all project
        pass
    else:
        # get uid's project
        pass
    
    # used for test
    # db_result = [[1, 2, 3, '2020-03-10'],
    #              [4, 5, 3, '2020-03-11']]

    db_result = np.array(db_result, dtype=np.str)
    return (list(db_result[:, id]), list(db_result[:, name]), list(db_result[:, status]), list(db_result[:, update_time]))
