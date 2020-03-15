# database utility

def select(para):#parameter
    #select name from employee where attribute1 = value1 
    #result: 'zhangsan'
    #para is a dictionary
    #para[select_key] = 'name'
    #para[select_value] = 'zhangsan'
    #para[tablename] = 'employee'
    #para[key] = 'attribute1'
    #para[value] = 'value1'
    
    # in table'work_time' not return delete label = 1
    #to do
    # return 'error' if key not found
    return status #'ok' or other

def update(para):
    #update project
    #set project_name = hh,main_function = nn
    #where project_id = 30
    #para[tablename] = 'project'
    #para[update_key] = 
    #para[update_value] = 
    #para[where_key] = 
    #para[where_value] =

    #todo
    # return 'error' if project_id not found else return 'ok'
    return status