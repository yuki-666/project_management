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
