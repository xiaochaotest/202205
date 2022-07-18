#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao
#创建类的普通方式
class Foo(object):
	def __init__(self,name):
		self.name=name

f=Foo('srli')

print(type(f))
print(type(Foo))

#创建类的特殊方式

def func(self):
	print('hello')

Fll = type('Fll',(object,),{'func':func})
'''
:type 第一个参数：类目
:type 第二个参数是当前类的基类
:type 第三个参数是类的成员
'''
fll=Fll()#实例化
fll.func()
print(type(Fll))