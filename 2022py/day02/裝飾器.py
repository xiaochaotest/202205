#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao
'''


装饰器：本质是函数，功能是用来装饰其他函数，给其他函数添加附加功能
原则：
1.不能修改被装饰的函数源代码
2.不能修改被装饰的函数的调用方式

高阶函数+嵌套函数=装饰器。
1.函数即‘变量’
2.高阶函数：
	a.把一个函数名当做一个实参传给另一个函数
	b.返回值汇总包含函数名
3.嵌套函数
'''
#在不修改被装饰函数源代码的情况下为其添加功能
# import time
# def osd():
# 	time.sleep(2)
# 	print('osdosd')
# def test(fun):
# 	star_time=time.time()
# 	fun()
# 	end_time=time.time()
# 	print('the func run time is %s'%(end_time-star_time))
# test(osd)

#不修改函数的调用方式
# import time
# def bar():
# 	time.sleep(2)
# 	print('is the bar')
#
# def test2(func):
# 	print(func)
# 	return func
# bar = test2(bar)
# bar()

#装饰器
# import time
# def spmia(func):
# 	def demo(*args,**kwargs):
# 		stat_time=time.time()
# 		func(*args,**kwargs)
# 		end_time=time.time()
# 		print('is the run time %s'%(end_time-stat_time))
# 	return demo
# @spmia
# def test1():
# 	time.sleep(2)
# 	print('is the test1...')
# @spmia
# def test2():
# 	time.sleep(3)
# 	print('is the test2...')
#
# test1()
# test2()
# user,passwd='axel','123'
# # def auth(func):
# # 	def wrapper(*args,**kwargs):
# # 		username=input('Username:').strip()
# # 		password=input('passwold:').strip()
# # 		if user==username and passwd==password:
# # 			print('登录成功')
# # 			return func(*args,**kwargs)
# # 		else:
# # 			exit('验证失败')
# # 	return wrapper
# #
# # def index():
# # 	print('weclome to index page')
# # @auth
# # def home():
# # 	print('weclome to index page')
# # 	return 'from home'
# # @auth
# # def bbs():
# # 	print('weclome to index page')
# #
# # index()
# # print(home())
# # bbs()



user,passwd='axel','123'
def auth(auth_type):
	print('auth func:',auth_type)
	def outer_wrapper(func):
			def wrapper(*args,**kwargs):
				print('auth func args:',*args,**kwargs)
				if auth_type=='local':
					username=input('Username:').strip()
					password=input('passwold:').strip()
					if user==username and passwd==password:
						print('登录成功')
						return func(*args,**kwargs)
					else:
						exit('验证失败')
				elif auth_type=='ldap':
					print('xxxxxxxx')
			return wrapper
	return outer_wrapper




def index():
	print('weclome to index page')
@auth(auth_type='local')
def home():
	print('weclome to index page')
	return 'from home'
@auth(auth_type='ldap')
def bbs():
	print('weclome to index page')

index()
print(home())
bbs()