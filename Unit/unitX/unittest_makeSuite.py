#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao
'''测试套件
1.测试套件就是测试用例的容器，把测试用例一个一个放进去
2.按顺序执行测试用例
'''
import unittest
import time as t
from selenium import webdriver
class BaiduTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		#打开要测试的浏览器
		cls.driver = webdriver.Firefox()
		#浏览器最大化
		cls.driver.maximize_window()
		#隐士等待3s
		cls.driver.implicitly_wait(30)
		#访问百度站点
		cls.driver.get('http://baidu.com')
	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
	#编写测试用例，建议使用编号命名，一定要加上注释
	def test_baidu_so_001(self):
		'''搜索业务：测试百度搜索'''
		self.driver.find_element_by_id("kw").send_keys("selenium")
		t.sleep(3)
		self.driver.get('http://baidu.com')
		print('001')

	def test_baidu_new_002(self):
		'''首页业务：点击百度新闻'''
		self.driver.find_element_by_link_text('新闻').click()
		t.sleep(3)
		self.driver.get('http://baidu.com')
		print('001111')
	def test_003(self):
		print('002222')
	def test_004(self):
		print('0033333')

if __name__ == '__main__':
	'''按测试类执行'''
	suite = unittest.makeSuite(BaiduTest)
	unittest.TextTestRunner(verbosity=2).run(suite)