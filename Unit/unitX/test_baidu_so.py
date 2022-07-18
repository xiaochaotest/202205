#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao
'''
单元测试框架：
测试固件（又叫钩子方法）：
1.当一个测试用例执行的时候，先执行setup()
2.接着执行XXX测试用例
3.最后执行tearDown()方法
实现只打开一次浏览器和关闭一次浏览器，使用测试固件（类方法  @classmathod)

测试套件，就是测试用例的集合




'''
import unittest
from selenium import webdriver
import time as t
from Unit.unitX.init import Init
#class UnitTest(unittest.TestCase):
class UnitTest(Init):
	'''
	#测试固件,使用setup()，每执行一次用例测试固件都会执行一次，这样有利有弊，所以需要改造使用@classmethod-->setupclass
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')
		print ('start')
	def tearDown(self):
		self.driver.close()
		print("come_over")
	'''
	# def setUp(self):
	# 	self.driver = webdriver.Firefox()
	# 	self.driver.maximize_window()
	# 	self.driver.implicitly_wait(30)
	# 	self.driver.get('http://www.baidu.com')
	#
	# def tearDown(self):
	# 	self.driver.close()

	def test_baidu_so_001(self):
		'''搜索业务：测试百度的搜索'''
		self.driver.find_element_by_id("kw").send_keys("python")
		self.driver.find_element_by_id("su").click()
		#使用classmethod要注意初始化的事情
		#self.driver.get("http://www.baidu.com")
		t.sleep(3)
	def test_baidu_sosuoyihou_002(self):
		'''断言百度搜索跳转的页面有如下内容'''
		so = self.driver.find_element_by_class_name("nums_text")
		self.assertEqual(so,'百度为您找到相关结果约100,000,000个')

		def test_baidu_so_title_003(self):
			'''首页业务：测试百度头部信息是否正确'''
			self.assertEqual(self.driver.title, 'python_百度搜索')

	def test_baidu_new(self):
		'''首页业务：点击百度新闻'''
		self.driver.find_element_by_link_text('新闻').click()
		self.driver.get("http://www.baidu.com")
		t.sleep(3)

	def test_baidu_shouye(self):
		'''首页业务：测试百度头部信息是否正确'''
		self.assertEqual(self.driver.title,'百度一下，你就知道')
	# def test_baidu_new(self):
	# 	#点击百度新闻
	# 	self.driver.find_element_by_link_text('新闻').click()
	# 	self.driver.get("http://www.baidu.com")
	# 	t.sleep(3)
	# @unittest.skip
	# def test_001(self):
	# 	pass
	# @unittest.skip("忽略这个测试用例执行")
	# def test_002(self):
	# 	pass
if __name__ == '__main__':
	'''对TestSuite进行实例化.。。ord（str2=‘n’）'''
	# suite=unittest.TestSuite()
	# suite.addTest(UnitTest('test_baidu_so'))
	# suite.addTest(UnitTest('test_baidu_new'))
	# unittest.TextTestRunner(verbosity=2).run(suite)
	#按测试类执行
	# suite = unittest.makeSuite(UnitTest)
	# unittest.TextTestRunner(verbosity=1).run(suite)
	unittest.main(verbosity=2)
