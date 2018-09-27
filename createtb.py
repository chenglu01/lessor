#!/env/pathon
#-*- coding:utf-8 -*-

#导入数据库模块
import MySQLdb

#打开数据库连接
db = MySQLdb.connect('localhost','root','123.com','testdb')

#使用游标定位数据库游标
cursor = db.cursor()

#使用execute执行SQL语句判断表是否存在
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

#创建SQL
sql = '''CREATE TABLE EMPLOYEE(
         first_name varchar(255) not null,
         last_name  varchar(255),
         age  int,
         sex char(1),
         income float)'''

#执行sql
cursor.execute(sql)

#关闭数据库
db.close()
