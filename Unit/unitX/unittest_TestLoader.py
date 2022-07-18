#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Peng Chao
'''
单元测试框架：
TestLoader




'''
import unittest
import time as t
from unitX.init import Init

class UnitTest(Init):
	def test_baidu_so(self):
		#测试百度的搜索
		self.driver.find_element_by_id("kw").send_keys("python")
		#使用classmethod要注意初始化的事情
		self.driver.get("http://www.baidu.com")
		t.sleep(3)

	def test_baidu_new(self):
		# 点击百度新闻
		self.driver.find_element_by_link_text('新闻').click()
		self.driver.get("http://www.baidu.com")
		t.sleep(3)

	def test_baidu_shouye(self):
		self.assertEqual(self.driver.title,'百度一下，你就知道')

if __name__ == '__main__':
	'''加载测试套件，按测试类.TestLoader()可以加载测试类'''
	suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
	unittest.TextTestRunner(verbosity=2).run(suite)