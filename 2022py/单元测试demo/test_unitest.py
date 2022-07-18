#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

import unittest

class Demo(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		print('setUpclass')
	@classmethod
	def tearDownClass(cls) -> None:
		print('deardownclass')

	def setUp(self) -> None:
		print('setUP')
	def tearDown(self) -> None:
		print('teardowm')

	def test_case01(self):
		print('这是第一条测试用例')
		self.assertEqual(2,2,'判断相等')
		self.assertNotIn('e','this')#前面值不在后值里面
		self.assertIn('h','this')#前值在后值里面

	def test_case02(self):
		print('这是第er条测试用例')
		self.assertEqual(2,2,'判断相等')
		self.assertNotIn('e','this')#前面值不在后值里面
		self.assertIn('h','this')

	@unittest.skipIf(1+1==2,'跳过这条用例')
	def test_case03(self):
		print('这是第san条测试用例')
		self.assertEqual(2,2,'判断相等')
		self.assertNotIn('e','this')#前面值不在后值里面
		self.assertIn('h','this')

class Demo1(unittest.TestCase):
	def test_demo1_case01(self):
		print('test_demo1_case01')
	def test_demo1_case02(self):
		print('test_demo1_case02')



if __name__ == '__main__':
	#unittest.main()#全部执行
	suite=unittest.TestSuite()
	suite.addTest(Demo('test_case01'))
	suite.addTest(Demo1('test_demo1_case02'))
	unittest.TextTestRunner().run(suite)