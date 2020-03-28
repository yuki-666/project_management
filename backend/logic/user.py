import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))
import config
import util.db as d

def get_project_superior():
    # return all project_superior
    # return (project_superior_id, project_superior_name)
    p = {}
    p['select_key'] = ['distinct project.project_superior_id','employee.name']
    p['tablename'] = 'project'
    p['join_tablename'] = ['employee']
    p['on_key'] = ['project.project_superior_id']
    p['on_value'] = ['employee.id']
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.selectDB(d.selectSql(p))

def get_custom():
    # return all custom
    # return (custom_id, company_name)
    p = {}
    p['select_key'] = ['distinct id','company_name']
    p['tablename'] = 'customer'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.selectDB(d.selectSql(p))

def get_total_user(project_id=None):
    p={}
    p['select_key'] = ['id','name']
    p['tablename'] = 'employee'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(d.selectSql(p))
    # return total user in company
    if project_id is not None:
        # status: if user in project
        # return uid, name, status
        p['select_key'] = ['person_id']
        p['tablename'] = 'project_participant'
        p['key'] = ['project_id']
        p['value'] = [' = '+project_id]
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        worker_in = db.selectDB(d.selectSql(p))
        w_list = []
        for i in worker_in:
            w_list.append(i['person_id'])
        for i in res:
            if i['id'] in w_list:
                i['status'] = 1
            else :
                i['status'] = 0
    return res

 
