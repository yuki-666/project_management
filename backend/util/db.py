import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))

import config
import pymysql

class ConnectToMysql(object):
    def __init__(self,host,username,password,database,port):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, self.port, charset='utf8', autocommit=True)
        self.cursor = self.db.cursor()
    
    def otherDB(self,sql): #增删改
        try:
            if self.cursor.execute(sql) == 0:
                return 'none' # 无数据符合where条件或改了和没改一样
            else:
                return 'ok'
        except:
            print('You have an error in your SQL syntax;') # sql语句有问题或其他问题
            self.db.rollback()
        finally:
            self.cursor.close()
            
    def selectDB(self, sql):   #查询
        try:
            if self.cursor.execute(sql) == 0:
                return 'Empty'  #查询无数据
            data = self.cursor.fetchall()
            desc = self.cursor.description  #转化为字典序
            output_data = [dict(zip([col[0] for col in desc], row)) for row in data]
            return output_data #输出字典型数据
        except:
            print('You have an error in your SQL syntax;')  #sql语句有问题或其他问题
        finally:
            self.cursor.close()
             
    def __del__(self):   #关闭连接
          self.cursor.close()
          self.db.close()

def selectSql(p):
    sql = '''select distinct ''' + p['select_key'][0]
    for i in range(1,len(p['select_key'])):
        sql = sql + ''' ,  ''' + p['select_key'][i] 
    sql = sql + ''' from '''
    if 'join_tablename' in p:
        sql_join = p['tablename'] + ' join ' + p['join_tablename'][0]
        if 'on_key' in p:
            sql_join = sql_join + ' on ' + p['on_key'][0] + ' = ' + p['on_value'][0]
        for i in range(1,len(p['join_tablename'])):
            sql_join = ' ( ' + sql_join + ' ) join ' + p['join_tablename'][i] + ' on ' + p['on_key'][i] + ' = ' + p['on_value'][i]
        sql = sql + sql_join
    else :
        sql = sql + p['tablename']
    if 'key' in p:
        sql = sql + ''' where ''' + p['key'][0] + p['value'][0]
        for i in range(1, len(p['key'])):
            sql = sql + ''' and ''' + p['key'][i] + p['value'][i]
    if 'sentence' in p:
        sql = sql + p['sentence']
    sql = sql + ''';'''
    # print(sql)#结项再删
    return sql

def updateSql(p):
    sql = '''update ''' + p['tablename'] + ''' set ''' + p['set_key'][0] + ''' = '%s' ''' % p['set_value'][0]
    for i in range(1,len(p['set_key'])):
        sql = sql + ''' , ''' + p['set_key'][i] + ''' = '%s' ''' % p['set_value'][i]
    if len(p['where_key'])>0:
        sql = sql + ''' where ''' + p['where_key'][0] + p['where_value'][0]
        for i in range(1,len(p['where_key'])):
            sql = sql + ''' and ''' + p['where_key'][i] + p['where_value'][i]
    sql = sql + ''';'''
    # print(sql)#结项再删
    return sql

def insertSql(p):
    #INSERT INTO table_name (column1,column2,column3,...) VALUES (value1,value2,value3,...);
    sql = '''insert into ''' +p['tablename']
    if 'column' in p:
        sql = sql + ' ( ' + p['column'][0]
        for i in range(1,len(p['column'])):
            sql = sql + ' ,  ' + p['column'][i]
        sql = sql + ' ) '
    sql = sql + ''' VALUES ('%s'   ''' % p['values'][0]
    for i in range(1,len(p['values'])):
        sql = sql + ''' ,'%s'   ''' % p['values'][i]
    sql = sql + ' ); '
    # print(sql)#结项再删
    return sql

def deleteSql(p):
    #INSERT INTO table_name (column1,column2,column3,...) VALUES (value1,value2,value3,...);
    sql = '''delete from ''' +p['tablename']
    if 'key' in p:
        sql = sql + ' where ' + p['key'][0] + p['value'][0]
        for i in range(1,len(p['key'])):
            sql = sql + ' and  ' + p['key'][i] + p['value'][i]
    sql = sql + ' ; '
    # print(sql)#结项再删
    return sql


