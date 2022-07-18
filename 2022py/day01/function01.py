#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao
# import time
# # def logger():
# #
# # 	time_format='%Y-%m-%d %X'
# # 	time_current=time.strftime(time_format)
# # 	with open('a.txt','w')as f:
# # 		f.write('%s end action\n'%time_current)
# #
# # def test1():
# # 	print('in the tetst1')
# # 	logger()
# # def test2():
# # 	print('in the test2')
# # def test3():
# # 	print('in the test3')
# #
# # test1()
# # test2()
# # test3()
# def t1():
# 	pass
# def t2():
# 	pass
# def t3():
# 	return 0,'hello',['a','b'],{'name':'wt'}
# x=t1()
# y=t2()
# z=t3()
# print(z)

#*args接收N个位置参数，转为元组
# def f1(*args):
# 	print(args)
# f1(2,2,'stae')
# f1(*[1,2,4,5,5])
#
# def f2(x,*args):
# 	print(x)
# 	print(args)
# f2(12,3,4,55,24)
# #接收N个关键字参数，转换为字典
# def a(**kwargs):
# 	print(kwargs)
# 	print(kwargs['name'])
# 	print(kwargs['age'])
# a(name='ax',age=12)
#
#
# #局部变量
# def xr(name):
# 	print('名字是%s'%name)
# 	age=33
# 	print('年龄是%s'%age)
# xr('炸群能干')
# name1 = 'wangti'
#
# def r1(name):
# 	#global name1
# 	name1 = 'zanghn'
# 	print(name,name1)
# 	age =13
# 	print(age)
#
# r1('wang')
#嵌套函数
# name2 ='wlw'
# def change_name():
# 	name2='wlw2222'
# 	def change_name1():
# 		name2='wlw333'
# 		print('第三层打印：',name2)
# 	change_name1()#调用内层函数
# 	print('第二次打印',name2)
# change_name()
# print('最外层打印：',name2)

#递归函数
def calc(n):
	print(n)
	if int(n/2)==0:
		return n
	return calc(int(n/2))
calc(10)

#进度条
import sys,time
for i in range(20):
	sys.stdout.write('#')
	sys.stdout.flush()
	time.sleep(0.1)