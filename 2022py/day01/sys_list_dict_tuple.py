#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao
'''
内置函数

'''

# import sys
# import os
#
# print(sys.path)
# print(sys.argv)
#
# print(os.system('dir')) #只读取不保存
# #打印内存地址
# print(os.popen('dir'))
# #打印内容
# r = os.popen('dir').read()
# print(r)

'''
list
'''
name = ['张三','老师','哇哇','alix','salary','lurl']
print(name)
print(name[0])#张三
print(name[-1])#salary
#切片取多个元素
#取下标1-4之间的值，包括1不包括4
print(name[1:4])#['老师', '哇哇', 'alix']
#取下标1至-1的值，不包括-1
print(name[1:-1])#['老师', '哇哇', 'alix', 'salary']
#从头开始取,0可以忽略
print(name[:3])#['张三', '老师', '哇哇']
#如果取最后一个，只能这样写
print(name[3:])#['alix', 'salary', 'lurl']
#这样写不会包含最后一个
print(name[3:-1])#['alix', 'salary']
#后面的2是代表每隔一个元素就取一个PS:0可忽略
print(name[0::2])#['张三', '哇哇', 'salary']

#步长切片
print("步长切片：",name[:4:2])

#追加
name.append('wttw')#['张三', '老师', '哇哇', 'alix', 'salary', 'lurl', 'wttw']
#插入
name.insert(1,'强行从老师前面插入')
#修改
name[1]='修改张三'
#删除
# del name[1]
# #删除指定元素
# name.remove('哇哇')
# #删除最后一个值
# name.pop()
#扩展
# s = [1,2,3]
# name.extend(s)
#拷贝
name_copy=name.copy()
print(name_copy)
#浅拷贝
import copy
s = ["name",["ssr",2234]]
p1=copy.copy(s)
print("p1:",p1)

p2=s[:]
print("p2:",p2)
p3 = list(s)
print("p3:",p3)


#排序
name.sort()
print('排序',name)
#反转
name.reverse()



print(name)

'''
元组,元组不可变
'''
name = ("zahngs","wangw","lisi")
print(name.count('lisi'))
print(name.index('lisi'))


'''购物车练习'''
# product_ilst =[
# 	('iphon',5990),
# 	('mac pro',8799),
# 	('bike',349),
# 	('watch',20093),
# 	('coffee',200)
# ]
# shoping = []
# salary=input('请输入工资：')
# if salary.isdigit():
# 	salary=int(salary)
# 	while True:
# 		# for item in product_ilst:
# 		# 	print(product_ilst.index(item),item)
# 		for index,item in enumerate(product_ilst):
# 			print(index+1,item)
# 		user_choice = input("选择要购买的商品>>>:")
# 		if user_choice.isdigit():
# 			user_choice=int(user_choice)
# 			if user_choice<=len(product_ilst) and user_choice>0:
# 				pr_item = product_ilst[user_choice]
# 				if pr_item[1]<=salary:
# 					salary-=pr_item[1]
# 					shoping.append(pr_item)
# 					print("你购买的商品%s,你的余额%s" %(shoping,salary))
# 				else:
# 					print('余额不足')
# 			else:
# 				print('非法输入')
# 		elif user_choice=='q':
# 			print('------购买的商品-----')
# 			for i in shoping:
# 				print(i)
# 			exit("你的余额：%s" %(salary))
# 		else:
# 			print("你的输入有误，请重新输入：")
'''
字典：字典是无序的，key必须是唯一的，天生去重
'''

info = {
	'stu1001':'Tenlgu',
	'stu1002':'Longzu',
	'stu1003':'xiaoze'
}
# #增
# info['stu1004'] = '罔替'
# #删
# info.pop('stu1003')
# info.popitem() #随机删
# del info['stu1001']
# #改
# info['stu1002']='龙珠'
# #查
# info.get('stu1002')
# print('stu1002' in info)
#
#
# print(info)


#多级字典嵌套操作
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
av_catalog['大陆']['1024'][1]+=',可以用爬虫爬下来！'

#输出所有的values
print(av_catalog.values())
#输出所有的key
print(av_catalog.keys())
print(av_catalog['大陆']['1024'])
#先去字典里面去取key，如果取不到再赋值一个新的
av_catalog.setdefault('大陆',{'www.baidu.com':[1,2]})

s={
	'大陆':'成都',
	'菲律宾':'非洲'
}
av_catalog.update(s)

print(av_catalog)
#字典转列表
print(av_catalog.items())


# info.fromkeys([1,2,3])
# print(info.fromkeys([1,2,3],'wangti'))

#循环
print('------循环------')
for i in av_catalog:
	print(i,av_catalog[i])
#该方法会讲字典转为列表，数据量大的时候不要用
for k,v in av_catalog.items():
	print(k,v)


'''
三级菜单练习
'''
# menu = {
#     '北京':{
#         '海淀':{
#             '五道口':{
#                 'soho':{},
#                 '网易':{},
#                 'google':{}
#             },
#             '中关村':{
#                 '爱奇艺':{},
#                 '汽车之家':{},
#                 'youku':{},
#             },
#             '上地':{
#                 '百度':{},
#             },
#         },
#         '昌平':{
#             '沙河':{
#                 '老男孩':{},
#                 '北航':{},
#             },
#             '天通苑':{},
#             '回龙观':{},
#         },
#         '朝阳':{},
#         '东城':{},
#     },
#     '上海':{
#         '闵行':{
#             "人民广场":{
#                 '炸鸡店':{}
#             }
#         },
#         '闸北':{
#             '火车战':{
#                 '携程':{}
#             }
#         },
#         '浦东':{},
#     },
#     '山东':{},
# }
#
# exit_flag = False
# while not exit_flag:
# 	for i in menu:
# 		print("打印第一层：",i)
# 	pofile = input("选择进入1：")
# 	if pofile in menu:
# 		while not exit_flag:
# 			for i1 in menu[pofile]:
# 				print("打印第二层",i1)
# 			pofile1 = input("选择进入2：")
# 			if pofile1 in menu[pofile]:
# 				while not exit_flag:
# 					for i2 in menu[pofile][pofile1]:
# 						print("打印第三层：",i2)
# 					pofile2 = input('选择进入3：')
# 					if pofile2 in menu[pofile][pofile1]:
# 						while not exit_flag:
# 							for i3 in menu[pofile][pofile1][pofile2]:
# 								print('打印第四层：',i3)
# 							pofile3=input('选择进入底层：')
# 							if pofile3 in menu[pofile][pofile1][pofile2]:
# 								while not exit_flag:
# 									for i4 in menu[pofile][pofile1][pofile2][pofile3]:
# 										print('打印第四层：',i4)
# 							elif pofile3 =='b':
# 								break
# 							elif pofile3 =='q':
# 								pass
# 							else:
# 								print('已经到底层了！')
# 								break
#



print("========集合==========")

'''
集合是一个无序的，不重复的数据组合
'''
s=[12,3,4,21,4,54]
s1 = set(s)
print(s1,type(s1))
s2=set([1,32,21,43,54])
print(s2,type(s2))

#取交集{21, 54}
print(s2.intersection(s1))
print(s2 & s1)
#取并集{32, 1, 3, 4, 43, 12, 21, 54}
print(s2.union(s1))
print(s2 | s1)
#取差集{32, 1, 43}
print(s2-s1)
print(s2.difference(s1))
#取对称差集{32, 1, 3, 4, 43, 12}
print(s2^s1)
print(s2.symmetric_difference(s1))
#取子集False
print(s2.issubset(s1))

#添加一项
s2.add('rr')

#添加多项
s2.update(['1','reset'])
print(s2)
#删除一项
print("删除一项",s2.remove(43))


print("集合的长度：",len(s2))
print("s2是否是S1的成员：",s2 in s1)
print('s2是否不是s1的成员：',s2 not in s1)
print("s2中每个元素都在s1中：",s2.issubset(s1))#s2 <= s1
print('s1中的每个元素都在s2中：',s2.issuperset(s1))#s2>=s1
print('返回一个新的集合，包含s1，s2的每个元素',s2.union(s1))#s2 | s1