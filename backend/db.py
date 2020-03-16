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


    def othertDB(self,sql): #增删改
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('ok')  #操作成功
        except:
            print('error') #sql语句有问题或其他问题
            self.db.rollback()
        finally:
            self.cursor.close()

            
    def selectDB(self,sql):   #查询
        try:
            self.cursor.execute(sql) 
            data = self.cursor.fetchall()
            desc = self.cursor.description  #转化为字典序
            output_data = [dict(zip([col[0] for col in desc], row)) for row in data]
            if(len(data)==0):
                print('Empty')  #查询无数据
            else:
                print(output_data) #输出字典型数据
        except:
            print('Error: unable to fecth data')  #sql语句有问题或其他问题
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
    sql="select username from login where id='0018'"
    #调用函数
    db.selectDB(sql)







            

    
