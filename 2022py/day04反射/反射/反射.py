#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao
'''
反射：
hasettr:判断一个对象里是否有对应的字符串的方法映射
getattr:根据字符串去获取对象里对应方法的内存地址
setattr:通过字符串设置新值
delattr:根据字符串的形式去某个模块做删除
'''
def bulk(self):
	print('%s is yelling....'%self.name)

class Dog(object):

	def __init__(self,name):
		self.name=name

	def eat(self,food):
		print('%s is eating...%s'%(self.name,food))

d=Dog('花花')
choice=input('>>>:').strip()

if hasattr(d,choice):#判断d里面是否有choice输入的对应方法
	funx = getattr(d,choice)#根据choice字符串去获取d对象里的对应方法的内存地址
	funx('wangti')
	print(getattr(d,choice))
	#删除
	#delattr(d,choice)
else:

	#动态装一个方法
	#setattr(d,choice,bulk)
	#d.s(d)
	#动态装一个属性
	setattr(d,choice,32)
	print(getattr(d, choice))

print(d.name)

