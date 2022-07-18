#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao



'''
静态方法
只是名义上归类管理，实际上在静态方法里访问不了类或实例中的属性

'''
class Dog(object):
	n=443

	def __init__(self,name):
		self.name=name

	@classmethod#类方法只能访问类变量，不能访问实例变量
	def eat(self):
		print('%s is eating...%s'% (self.n,'狗粮'))

	def talk(self):
		print('%s is talking...'%self.name)

d=Dog('旺财')
d.eat()