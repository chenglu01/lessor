#!/env/python
#-*- coding:utf-8 -*-

#导入socket模块
import socket

#创建socket对象
s = socket.socket()

#获取本机主机名
host = socket.gethostname()

#设置端口号
port = 1888

#连接主机
s.connect((host,port))

#打印接受到的数据
print s.recv(1024)

#关闭连接
s.close()
