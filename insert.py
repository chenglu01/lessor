#!/env/pathon
#-*- coding: utf-8 -*-

#导入数据库模块
import MySQLdb

#打开数据库连接
db = MySQLdb.connect('localhost','root','123.com','testdb')

#使用cursor()方法获取数据库操作游标
cursor = db.cursor()
fname = 'cheng'
lname = 'lu'
#创建sql语句

sql = "INSERT INTO EMPLOYEE(first_name,last_name,age,sex,income)\
         VALUES('%s','%s','%d','%c','%d')" \
         % (fname,lname,21,'m',113000)

#使用execute执行sql语句
#异常捕获
try:
    cursor.execute(sql)
#提交到数据库
    db.commit()
except:
#发生异常时回滚
    db.rollback() 

#关闭sql
db.close()
