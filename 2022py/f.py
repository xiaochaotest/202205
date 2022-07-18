#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:pc

'''
注册账户，然后登录到系统后，显示出登录的昵称

'''

def register():
	'''实现账户的注册'''
	username=input('请输入账号：\n')
	password=input('请输入密码：\n')
	temp=username+'|'+password
	with open('user.txt','w')as f:
		f.write(temp)
def login():
	'''登录'''
	with open('user.txt','r')as f:
		info=f.read()
		print(info)

login()