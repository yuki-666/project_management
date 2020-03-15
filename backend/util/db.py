# database utility

def select(para):#parameter
    #select name from employee join table_a where attribute1 = value1 and employee.xx = table_a.yy
    #result: 'zhangsan'
    #para is a dictionary
    #para[select_key] = ['name']
    #para[select_value] = ['zhangsan']
    #para[tablename] = 'employee'
    #para[join_tablename] = ['table_a']
    #para[key] = [where 子句等号左边]
    #para[value] = [where 子句等号右边]
    
    #to do
    # return 'error' if key not found
    return status #'ok' or other

def update(para):
    #update project
    #set project_name = hh,main_function = nn
    #where project_id = 30
    #para[tablename] = 'project'
    #para[set_key] = 
    #para[set_value] = 
    #para[where_key] = 
    #para[where_value] =

    #todo
    # return 'error' if project_id not found else return 'ok'
    return status