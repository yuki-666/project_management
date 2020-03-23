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
        self.db = pymysql.connect(self.host,self.username,self.password,self.database,self.port,charset='utf8')
        self.cursor = self.db.cursor()
    
    def otherDB(self,sql): #增删改
        try:
            if self.cursor.execute(sql) == 0:
                return 'none'#无数据符合where条件
            else :
                return 'ok'
            self.db.commit()
        except:
            #print('You have an error in your SQL syntax;') #sql语句有问题或其他问题
            self.db.rollback()
        finally:
            self.cursor.close()

            
    def selectDB(self,sql):   #查询
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
    sql = '''select ''' + p['select_key'][0]
    for i in range(1,len(p['select_key'])):
        sql = sql + ''', ''' + p['select_key'][i] 
    sql = sql + ''' from ''' + p['tablename'] 
    if len(p['join_tablename'])>0:
        sql = sql + ''' join ''' + p['join_tablename'][0]
        for i in range(1,len(p['join_tablename'])):
            sql = sql + ''',''' + p['join_tablename'][i] 
        if len(p['on_key'])>0:
            sql = sql + ''' on ''' + p['on_key'][0] + ''' = '''+p['on_value'][0]
            for i in range(1,len(p['on_key'])):
                sql = sql + ''' and ''' + p['on_key'][i] + ''' = '''+p['on_value'][i]
    if len(p['key'])>0:
        sql = sql + ''' where ''' + p['key'][0] + p['value'][0]
        for i in range(1,len(p['key'])):
            sql = sql + ''' and ''' + p['key'][i] + p['value'][i]
    sql = sql + ''';'''
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
    return sql

#使用实例
if __name__ == '__main__':
    #创建连接
    db = ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    #sql语句
    sql = "select username from login where id='0012'"
    #调用函数
    print(db.selectDB(sql))
