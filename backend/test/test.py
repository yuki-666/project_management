import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))
import logic.login
import logic.project as p
import logic.user as u
import logic.work_time as w

if __name__ == '__main__':
    
    #print(logic.login('卡桑','000111'))  
   #print(logic.login('费费','111222'))  
   #print(logic.login('工具人','555666'))  
    #print(logic.login('not exist','kk'))
    #print(logic.login('卡桑','password error'))
    #print(logic.search_project(project_id = '01'))
    #print(logic.search_project(keyword = '0'))
    #print(logic.search_project(keyword = '系统'))
    #print(logic.search_project())
    #print(logic.get_project(0,0,None,False))
    #print(logic.get_project(0,0,None,True))
    #print(logic.get_project(0,0,'01',False))
    #print(logic.get_project(0,0,'0011',True))

    #print(logic.modify_project('01', 'name', 'good','2020-9-8', '2020-10-9', '0000', 'major_milestones', 'adopting_technology', 'business_area', 'main_function'))  
    #print(logic.confirm_project('01',2))
    #print(logic.get_work_time_by_uid('0000'))
    #print(logic.get_work_time_by_uid('0000',is_superior=True))
    #print(logic.get_work_time_by_uid('0011',include_finished=True))
    #print(logic.get_work_time_by_work_time_id('2'))
    #print(logic.confirm_work_time('2', '0'))
    #print(logic.confirm_work_time('2', '2'))
    #print(logic.confirm_work_time('6', '2'))
    #print(logic.delete_work_time('6'))
    #print(logic.delete_work_time('2'))
    #print(logic.delete_work_time('11'))
    #print(logic.modify_word_time('3', 'fun2', 'e2', '2020-2-15-12:9:21', '2020-2-15-12:9:21'))
    #print(logic.modify_word_time('1', 'fun2', 'e2', '2020-2-15-12:9:21', '2020-2-15-12:9:21'))

    ########project.py
    #p.create('n1', 'describe', 'M', '2020-03-14', '2020-03-15', '0000', '001', 'first', 'vue', '金融', '打字')
    #print(p.create('n2', 'describe', 'D', '2020-03-14', '2020-03-15', '0000', '001', 'second', 'vue', 'financial', 'lent'))
    #p='02'
    #print(int(p[-2]+p[-1]))
    #print(p.get_info_include_work_time('0014'))
    #db = d.ConnectToMysql(config.host, config.username, config.password, config.database, config.port)
    #print(db.otherDB('insert into project(`id`,`name`) values(\'12\',\'n1\');'))

    ########user.py
    #print(u.get_project_superior())
    #print(u.get_custom())
    #print(w.get_info_by_uid_project_id('0012', '01'))
    #print(3/5)
    #print(u.get_total_user('01'))
    #print(u.get_total_user())
    #print(p.get_project_member(project_id='01', function_id=None))
    #print(p.get_project_member(project_id='01', function_id='01'))
    #a = [{'id': '0011', 'name': '卡桑', 'status': 0}, {'id': '0012', 'name': '小黄', 'status': 1}]
    #b = (a[0][0],a[0][1])
    #print(b)
    #print(p.get_function(project_id='02'))
    #print(p.get_children_function(project_id='02', parent_function_id='02'))
    #p.add_function(project_id='02', parent_function_id='002', function_name='拼单子功能')
    #print(p.delete_function(project_id='01', function_id='002'))
    #print(p.get_authority(project_id='01', uid='0012'))
    #print(p.get_authority(project_id='01'))
    #print(p.modify_authority(project_id='01', uid='0012', git_authority='0', file_authority='1', mail_authority='1'))
    #print(chr(ord('8')+1))
    #a=list('1ZZ')
    #p.add(a,2)
    #print(a)
    #a='8899999'
    #b=a[-3:]
    #print(b)
    #a=[2,3]
    #b=[2]
    #c=list(set(a)-set(b))
    #print(c)
    #p.modify_function(project_id='02', function_id='002004', function_name='拼单gg', uid=['0016','0017'])
    #p.modify_worker(project_id, uid)
    a='uu,ii'
    print(a.split(','))