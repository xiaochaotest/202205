#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao

import unittest
import os
import HTMLTestRunner

# def allRun():
# 	suite = unittest.TestLoader().discover(
# 		start_dir = os.path.dirname(__file__),
# 		pattern = 'test_*.py',
# 	top_level_dir = None)
# 	unittest.TextTestRunner(verbosity=2).run(suite)
# allRun()

#print (os.path.dirname(__file__))

def allTestCase():
	'''返回所有测试用例'''
	suite = unittest.defaultTestLoader.discover(
		start_dir=os.path.dirname(__file__),
		pattern = 'test_baidu_so.py',
		top_level_dir=None
	)
	return suite

def run():
	'''生成测试报告'''
	fp = open('testReport.html','wb')#测试报告放置得位置
	HTMLTestRunner.HTMLTestRunner(
		stream=fp,
	title='接口UI自动化测试报告',
	description='基于python的UI自动化测试报告').run(allTestCase())

run()