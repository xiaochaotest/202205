#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

class Flighe(object):
	def __init__(self,name):
		self.flight_name=name

	def checking_status(self):
		print('checking filght %s status'%self.flight_name)
		return 1

	@property
	def flight_status(self):
		status=self.checking_status()
		if status == 0 :
			print('飞机还没有起飞...')
		elif status==1:
			print('飞机起飞了...')
		elif status ==2:
			print('飞机降落了')
		else:
			print('飞机还没有航班')
	#修改
	@flight_status.setter
	def flight_status(self,status):
		print('%s飞机的状态改了%s'%(self.flight_name,status))
	#删除
	@flight_status.deleter
	def flight_status(self):
		print('status got removed....')

f=Flighe('CU9890')

f.flight_status

f.flight_status=0

del f.flight_status

