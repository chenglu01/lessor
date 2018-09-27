#!/env/python
#-*- coding: utf-8 -*-

#导入socket模块
import socket

#创建一个socket对象
s = socket.socket()

#获取本机主机名
host = socket.gethostname()
print host
#配置一个端口
port = 1888

#绑定主机名和端口
s.bind((host,port))

#等待客户端连接
s.listen(5)

while True:
    c, addr = s.accept()
    print "连接地址：" , addr
    c.send('欢迎接受socket信息')
    c.close()
