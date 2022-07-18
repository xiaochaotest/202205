#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao
'''
常用异常：
AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的

'''

name=['axle','jack']
data={}

#推荐写法，好定位问题
# try:
# 	name[3]
# 	data['name']
# except KeyError as e:
# 	print('name不存在',e)
# except IndexError as e1:
# 	print('列表操作错误',e1)

#可以同时捕获多种错误，不推荐这样写，这样写不知道是那段代码出错
try:
	#主代码块
	# name[3]
	# data['name']
	# open('test.txt')
	a=1
	print(a)
except (KeyError,IndexError) as e:
	#异常时执行该块
	print('name不存在',e)
except IndexError as e:
	print('列表操作错误',e)
except Exception as e:
	print('未知错误')
else:
	#主代码块执行完执行该块
	print('一切正常的情况执行')
finally:
	#无论异常与否最终都执行该块
	print('不管有没有错都执行')


# try:
# 	# name[3]
# 	# data['name']
# 	open('tes.txt')
# except Exception as e:#一般不用这种写法
# 	print('能抓到所有的错误',e)