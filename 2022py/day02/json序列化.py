#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

#文件只能存字符串或者二进制
# with open('test.txt','w')as f:
# 	info={
# 		'name':'zt0',
# 		'age':12
# 	}
# 	f.write(str(info))
# with open('test.txt','r')as f:
# # 	data = eval(f.read())
# # 	print(data['age'])
# # 	print(type(data))



#序列化dumps
# import json
# # with open('test1.txt','w',encoding='utf-8')as f:
# # 	info = {
# # 				'name':'张三',
# # 				'age':21
# # 		 	}
# # 	f.write( json.dumps(info))
# # #反序列化loads
# #
# # with open('test1.txt','r')as f:
# # 	data=json.loads(f.read())
# # 	print(data['age'])

import pickle
def x(name):
	print('hello!',name)
#pickle.dumps将数据通过特殊的形式转换为只有python语言认识的字符串
with open('test2.txt','wb')as f:
	f.write(pickle.dumps('rln你的，你的饭23'))


