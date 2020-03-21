import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))
import config
import util.db as d

def get_project(project_id=None, uid=None, keyword=None, detail=False, include_reject=False):
    # id | name      | status | customer_id | main_function
    #    | domain_id | tech   | project_leader_id | submit_date | reserve_date

    # check if only exist one type, or get all if == 0
    is_none_1, is_none_2, is_none_3 = project_id is not None, uid is not None, keyword is not None
    exist_param_count = is_none_1 + is_none_2 + is_none_3
    if exist_param_count > 1:
        return config.error_value

    # measure detail
    if detail == False:
        sql = '''select id, name, status, update_time '''
    else:
        sql = '''select id, name, status, update_time, describe, scheduled_time, delivery_day, project_superior_name, major_milestones, adopting_technology, business_area, main_function '''
    sql += 'from project '

    if keyword is not None:
        like = '%'
        for i in range(len(keyword)):
            like = like + keyword[i]
            like = like + '%'

        sql_id = sql + '''where id like '%s';''' % like
        sql_name = sql + '''where name like '%s';''' % like
        if include_reject == False:
            sql_id = sql_id[:-1] + ' and status > 0;'
            sql_name = sql_name[:-1] + ' and status > 0;'

        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        res_id = db.selectDB(sql_id)
        db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
        res_name = db.selectDB(sql_name)

        # merge and unique
        res = []
        if res_id != 'Empty':
            res += res_id
        if res_name != 'Empty':
            res += res_name
        res = [dict(j) for j in set([tuple(i.items()) for i in res])]
        return res

    if project_id is not None:
        sql += '''where id = '%s' ''' % project_id
    elif uid is not None:
        sql += '''join project_participant 
                  on project_participant.project_id = project.id 
                  where project_participant.person_id = '%s' ''' % uid

    # measure include_reject
    if include_reject == False:
        if exist_param_count == 0:
            # get all
            sql += 'where status > 0;'
        else:
            # project_id or uid
            sql += 'and status > 0;'
    
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.selectDB(sql)
    return [] if res == 'Empty' else res

if __name__ == '__main__':
    print(get_project(keyword='系统', include_reject=True))
