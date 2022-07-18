#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

class Role(object):
	age=12#类变量
	name='类变量'
	'''
	构造函数：
	在实例化时做一些类的初始化工作
	self其实就是实例本身，实例化的时候python会自动把这个实例本身通过self传进去

	'''
	def __init__(self, name, role, weapon, life_value=100, money=15000):
		self.name = name#实例变量（静态属性），作用域就是实例本身
		self.role = role
		self.weapon = weapon
		#私有变量
		self.__life_value = life_value
		self.money = money

	def __del__(self):
		#析构函数
		#在实例释放、销毁的时候执行，通常用于做一些收尾工作
		print('%s 战氏了 ' %self.name )

	def shot(self):
		print("shooting...")

	def got_shot(self):
		print("ah...,I got shot...")

	def buy_gun(self, gun_name):
		print("%s just bought %s" % (self.name,gun_name))
	#私有方法
	def __lift(self):
		self.__life_value-=50
		print('xueliang:%s' %self.__life_value)

#把一个类变成一个具体的对象叫实例化
r1 = Role('Alex', 'police', 'AK47') #实例化（初始化一个类）
r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色

r1.buy_gun('AK47')
r1.name='占三分'
r1.block='防弹衣'
print(r1.age, r1.name,r1.block)
print(r1.age)
print(r1.lift())

print('r2',r2.name)


#继承

