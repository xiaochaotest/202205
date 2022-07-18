#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

import os
#获取当前工作目录
print(os.getcwd())
#改变当前脚本工作目录
print(os.chdir(r'D:\\git\\2022py\\常用模块'))
#返回当前目录
print(os.curdir)
#获取当前目录的父目录字符串名
print(os.pardir)
#生成单级目录
#print(os.mkdir('单机目录'))
#删除单级空目录
#print(os.rmdir('单机目录'))
#列出指定目录下的所有文件和子目录
print(os.listdir(r'D:/git/2022py/常用模块'))
#删除一个文件
#os.remove()
#重命名文件/目录
#print(os.rename(r'D:/git/2022py/常用模块', r'D:/git/2022py/m常用模块'))

#获取文件/目录信息
print(os.stat('D:/git/2022py/常用模块'))
#输出操作系统指定的路径分隔符
print(os.sep)
#输出当前平台使用的行终止符
print(os.linesep)
#输出用于分割文件路径的字符串
print(os.pathsep)
#输出字符串指示当前使用平台
print(os.name)
#运行shell命令，直接显示
#print(os.system('cd'))
#获取系统环境变量
print(os.environ)
#返回path规范化的绝对路径
print(os.path.abspath(path='D:\git\2022py\常用模块'))
#将path分割成目录和文件名
print(os.path.split('D:\git\2022py\常用模块'))
#返回path的目录
print(os.path.dirname('D:\git\2022py\常用模块'))
#返回path最后的文件名
print(os.path.basename('D:\git\2022py\常用模块'))
#如果path存在返回True否则返回false
print(os.path.exists('D:\git\2022py\常用模块'))
#如果path是一个存在的目录则返回True否则false
print(os.path.isdir('D:\git\2022py\常用模块'))
#如果path是绝对路径放true，否则false
print(os.path.isabs('D:\git\2022py\常用模块'))
#将多个路径组合后返回
print(os.path.join('D:', '\git\2022py'))
#返回path所指向的文件或者目录的最后存取时间
#print(os.path.getatime('D:\git\2022py\常用模块\os模块.py'))
#打印执行模块的绝对路径
print("当前文件绝对路径：",os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
