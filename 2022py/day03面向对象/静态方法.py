#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao


'''
静态方法
只是名义上归类管理，实际上在静态方法里访问不了类或实例中的属性

'''
class Dog(object):

	def __init__(self,name):
		self.name=name

	@staticmethod#静态方法实际跟类没什么关系
	def eat(self):
		print('%s is eating...%s'% (self.name,'狗粮'))


d=Dog('旺财')
d.eat(d)