#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

import shelve
import datetime

d=shelve.open('shelve_test')
# class Test(object):
# 	def __init__(self,n):
# 		self.n=n
# t=Test(123)
# t1=Test(123334)



#写
# info={'age':22,'job':'it'}
# name = ['alex','rain','test']
# d['test']=name
# d['inifo']=info
# d['date']=datetime.datetime.now()
# d.close()


#读
print(d.get('name'))
print(d.get('info'))
print(d.get('date'))