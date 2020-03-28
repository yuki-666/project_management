import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))
import config
import util.db as d

def get_project_superior():
    sql = 'select id, name from employee where career = 0'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    return res

def get_custom():
    # return all custom
    # return (custom_id, company_name)
    p = {}
    p['select_key'] = ['distinct id','company_name']
    p['tablename'] = 'customer'
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.selectDB(d.selectSql(p))
    pass

def get_total_user(project_id=None):
    # TODO
    # return total user in company
    if project_id is not None:
        # status: if user in project
        # return uid, name, status
        pass
    else:
        # return uid, name
        pass
