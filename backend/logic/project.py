import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))
import config
import util.db as d

def get_info(project_id=None, uid=None, keyword=None, detail=False, include_reject=False):
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

def get_info_include_work_time(uid):
    # TODO
    # not include reject project
    # return (id, name, status, update_time, remain_work_time)
    pass

def confirm(project_id, status):
    # check if project status is 1 (pending), return 'error' if not
    # modify project status, from 1 to 0/2 (rejection/established)
    sql = '''update project set status = '%s' where id = '%s' and status =1;'''%(project_id,status)
    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    res = db.otherDB(sql)
    if res == 'ok':
        return 'ok'
    else :
        return 'error'

def modify(project_id, project_name, describe, scheduled_time, delivery_day, project_superior_id, major_milestones, adopting_technology, business_area, main_function):
    # modify project info, search by id
    sql = '''update project
    set name = '%s', describe = '%s' ,reserve_date = '%s',submit_date = '%s', project_leader_id = '%s',major_milestones = '%s',tech = '%s',domain_id = '%s',main_function ='%s'
    where id = '%s';''' %(project_name,  describe,scheduled_time, delivery_day, project_superior_id, \
    major_milestones, adopting_technology, business_area, main_function,project_id)
    
    # id | name  | status | customer_id | main_function 
    #    | domain_id | tech   | project_leader_id | submit_date | reserve_date | update_time     

    db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    return db.otherDB(sql)

def create(name, describe, development_type, scheduled_time, delivery_day, project_superior_id, custom_id, major_milestones, adopting_technology, business_area, main_function):
    # TODO
    # id:
    # '2020-1111-D-01'
    # 'date-customid-development_type-sequence_number'

    # date:取当前年份

    # sequence_number: 'date-customid-development_'为前缀的所有，取它们的sequence_number的max，再+1作为这次的sequence_number. 
    # 若是1位数前面添0, 若一个都没搜出来从1开始计数
    
    # id 由“四位年份-四位客户代码-研发类型 1 位（开发：D，维护：M，服务：S，其他：O）-顺序号 2 位”构成，且从外部系统导入，是一个选择项，不可更改。
    return 'ok'

def get_function(project_id):
    # TODO
    # get function list from project_id
    # worker_id and worker_name: list->str, split by ','
    # return function_id, function_name, worker_id, worker_name, parent_function_id
    pass

def get_children_function(project_id, parent_function_id):
    # TODO
    # get function list from project_id, whose parent function id == parent_function_id
    # worker_id and worker_name: list->str, split by ','
    # return function_id, function_name, worker_id, worker_name, parent_function_id
    pass

def get_project_member(project_id, function_id=None):
    # TODO
    if function_id is not None:
        # status: if user is in function
        # return uid, name, status
    else:
        # return uid, name
    pass

def add_function(project_id, parent_function_id, function_name)
    # TODO
    # new function id:
    # 1. last_function_id = max function_id starts with parent_function_id
    # 2. new_function_id = last_function_id + 1, 3 digits, each digit: 012……789abc……xyzABC……XYZ
    return 'ok'

def delete_function(project_id, function_id):
    # TODO
    # check if delete_label == 0, return 'error' if delete_label == 1
    # 1. set delete_label to 1
    # 2. set children functions' delete_label to 1 (children function: function id starts with function_id)
    return 'ok'

def modify_function(project_id, function_id, function_name, uid):
    # TODO
    # uid(split by ',') change to list
    return 'ok'

def modify_worker(project_id, uid):
    # TODO
    # uid(split by ',') change to list
    # update user participate in project
    return 'ok'

def get_authority(project_id, uid=None):
    # TODO
    if uid is not None:
        # return (git_authority, file_authority, mail_authority)
    else:
        # get total user in project
        # return (uid, name, git_authority, file_authority, mail_authority)

def modify_authority(project_id, uid, git_authority, file_authority, mail_authority):
    # TODO
    # if can't find project_id uid in table, return 'error'
    # update authority
    return 'ok'

if __name__ == '__main__':
    print(get_info(keyword='系统', include_reject=True))
