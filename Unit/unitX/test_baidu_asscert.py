import unittest
import time as t
from unitX.init import Init

class Baidu(Init):
	'''首页业务，测试百度的title是否正确'''
	def test_baidu_shouye(self):

		# print(type(self.driver.title))
		# print(type((u'百度一下，你就知道').encode('gbk')))
		self.assertEqual(self.driver.title, '百度一下，你就知道')
if __name__ == '__main__':
	'''加载测试套件，按测试类.TestLoader()可以加载测试类'''
	suite = unittest.TestLoader().loadTestsFromTestCase(Baidu)
	unittest.TextTestRunner(verbosity=2).run(suite)