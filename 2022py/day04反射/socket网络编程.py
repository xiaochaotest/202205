#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

'''
应用层
表示层
会话层
传输层
网络层
数据链路层
物理层
'''
#客户端
import socket

ip_port=('localhost',9999)
#定义协议
client=socket.socket()#声明socket类型，同时生成socket链接对象
client.connect(ip_port)


client.sendall('请求占领地球'.encode('utf-8'))
data=client.recv(1024)
print('recv:',data)
client.close()
