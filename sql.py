#!/env/python
#-*- coding: utf-8 -*-

#导入数据库模块
import MySQLdb

#打开数据库连接
db = MySQLdb.connect(host='dev-db.ehking.com',port=3309,user='ehking-dev',passwd='BmZyqzDmnsK3Q6eW',db='dev_eos')

#使用游标标记数据游标
cursor = db.cursor()

#使用execute执行sql语句
record_ecs_id = '47qhpMtkZniWyMojfi4sjC'
sql = "UPDATE aliyun_project_release_record_ecs SET status=4 WHERE id='%s'" % record_ecs_id
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

#关闭数据库

db.close()
