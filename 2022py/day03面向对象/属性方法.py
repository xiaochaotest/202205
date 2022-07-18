#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao


'''
静态方法
只是名义上归类管理，实际上在静态方法里访问不了类或实例中的属性

'''
class Dog(object):

	def __init__(self,name,food):
		self.name=name
		self.__food=food
	#把一个方法变成属性
	@property #属性方法就是把一个方法变成一个静态属性
	def eat(self):
		print('%s is eating...%s'% (self.name,self.__food))
	#修改属性方法
	@eat.setter
	def eat(self,food):
		print('set to food:',food)
		self.__food=food
	#删除
	@eat.deleter
	def eat(self):
		del self.__food
		print('删除')

d=Dog('旺财','面粉')
d.eat
d.eat='大米'

del d.eat

d.eat