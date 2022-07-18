#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao
'''
unittest第一节（unittest  第二节结束）
测试固件
'''
import unittest
from selenium import webdriver
import time as t

class BaiduTest(unittest.TestCase):
	def setUp(self):
		#打开要测试的浏览器
		self.driver = webdriver.Firefox()
		#浏览器最大化
		self.driver.maximize_window()
		#隐士等待3s
		self.driver.implicitly_wait(30)
		#访问百度站点
		self.driver.get('http://baidu.com')

	def tearDown(self):
		self.driver.close()
	#编写测试用例，建议使用编号命名，一定要加上注释
	def test_baidu_so(self):
		'''搜索业务：测试百度搜索'''
		self.driver.find_element_by_id("kw").send_keys("selenium")
		t.sleep(3)
	def test_baidu_new(self):
		'''首页业务：点击百度新闻'''
		self.driver.find_element_by_link_text('新闻').click()
		t.sleep(3)
if __name__ == '__main__':
	unittest.main(verbosity=2)