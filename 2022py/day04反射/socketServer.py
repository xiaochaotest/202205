#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

import socket

ip_port=('localhost',9999)

server=socket.socket()

server.bind(ip_port)#绑定要监听的端口
server.listen(3)#监听
print('我要开始等电话了')

conn,addr = server.accept()#等连接
#conn就是客户端连过来而在服务器端为其生成的一个连接实例
print(conn,addr )
print('电话来了')
data=conn.recv(1024)
print('recv:',data)
server.send(data.upper())
server.close()

