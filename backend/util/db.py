import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))

import pymysql
import tomysql #数据库基本信息

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


#使用实例
if __name__ == '__main__':
    #创建连接
    db = ConnectToMysql(tomysql.host,tomysql.username,tomysql.password,tomysql.database,tomysql.port)
    #sql语句
    sql = "select username from login where id='0012'"
    #调用函数
    print(db.selectDB(sql))
