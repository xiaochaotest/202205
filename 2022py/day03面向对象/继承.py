#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao
'''
新式类和经典类不同：其实就是在继承顺序上不同
深度优先
广度优先
python2经典类是深度优先继承，新式类是按广度优先继承
python3开始不论是经典类还是新式类都是广度优先来继承。

'''
#经典类
#class People:
#新式类
class People(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age


	def eat(self):
		print('%s is eating...' % self.name)

	def talk(self):
		print('%s is talking...' % self.name)

	def sleep(self):
		print('%s is sleeping...' % self.name)


class Relation(object):
	def make_friends(self,obj):
		print('%s is %s交朋友'%(self.name,obj.name))


class Man(People,Relation):
	def __init__(self,name,age,money):
		super(Man, self).__init__(name,age)#新式类写法
		#People.__init__(self,name,age)
		self.money=money
		print('%s一出生就有%s块钱'%(self.name,self.money))

	def pia(self):
		print('%s is pipaping..20s...done.'%self.name)

	def sleep(self):
		People.sleep(self)
		print('重写父类方法')

class Woma(Man,Relation):
	def __init__(self,name,age,money,sex):
		super(Woma, self).__init__(name,age,money)
		self.sex=sex
		print('%s的性别是%s'%(self.name,self.sex))

	def get_birth(self):
		print('%s birth...'%self.name)

#p=Man('alax',23,200)
# print(p.eat())
# print(p.pia())
# p.sleep()


m=Woma('花儿',24,5000,'女')
# #m.get_birth()
# p.make_friends(m)
#
#m.make_friends(p)