#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

class alexException(Exception):

	def __init__(self,msg):
		self.msg=msg

	def __str__(self):#定义返回格式，不写也可以。基类已经写了
		return 'rrrrrr.'
try:
	raise alexException('异常')
except alexException as e:
	print(e)
