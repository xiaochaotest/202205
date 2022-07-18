#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao
'''布尔类型断言'''

import unittest
from selenium import webdriver

class Sina(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://mail.sina.com.cn/')

	def tearDown(self):
		self.driver.quit()
	def test_sina_isLogin(self):
		'''新浪业务：判断登陆页面自动登陆按钮是否勾选'''
		isLogin = self.driver.find_element_by_id('store1').click()
		isLogin.is_selected()
		self.assertTrue(isLogin)

	if __name__ == '__main__':
	    unittest.main(verbosity=2)