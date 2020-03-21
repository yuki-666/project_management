import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))
import config
import util.db as d

def login(username, password):
    # login:id      | username  | password 
    # employee:id   | name      | gender    | career      
    # superior_id   | tele      | department| mailbox
    sql = '''select login.id,employee.career
             from login join employee
             on login.id = employee.id
             where login.username = '%s' and login.password = '%s';''' % (username, password)
    
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    
    if not res == 'Empty':
        if res[0]['career'] != None:
            return (0, res[0])

        # leader or worker
        sql = '''select 2 from project_participant join login
                 where login.username = '%s' and login.id = project_participant.leader_id;''' % username
                 
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        if db.selectDB(sql) == 'Empty':
            res[0]['career'] = '3'
            return (0, res)
        else:
            res[0]['career'] = '2'
            return (0, res)
    else :
        sql = '''select login.id,employee.career
             from login join employee
             on login.id = employee.id
             where login.username = '%s';''' % username

        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        res = db.selectDB(sql)
        if res == 'Empty':
            return 1
        else:
            return 2
