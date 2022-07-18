#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

#__doc__表示类的描述信息
# class Fll:
# 	'''
#
# 	描述类信息。。
# 	'''
# 	def func(self):
# 		pass
# print(Fll.__doc__)#输出类的描述信息
#print(Fll.__module__)#输出当前操作的对象在哪个模块
#print(Fll.__class__)#表示当前操作的对象的类是什么
#__init__构造方法，通过类创建对象时，自动触发执行
#__del__析构方法，当对象在内存中被释放时，自动触发执行

#构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
# class Foo:
#
# 	def __init__(self):
# 		pass
#
# 	def __call__(self, *args, **kwargs):
# 		print( '__call__')
#
#
# obj = Foo()  # 执行 __init__
# obj()  # 执行 __call__

