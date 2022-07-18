#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

import random

#生成0-1的随机浮点数
print(random.random())
print(random.uniform(1, 10))
#生成1-2的随机数
print(random.randint(1,2))
#生成1-9的随机数
print(random.randrange(1, 10))
#随机从字符串中取值
print(random.choice('2sdfewc'))
#多个字符中取特定数量的字符
print(random.sample('3sdafgae4rtwq',3))
#取随机整数
print(random.randint(1, 33))
#随机选取0-100之间的偶数
print(random.randrange(1, 101, 2))
#随机选取字符串
print(random.choice(['ds', 'fer', 'sa']))
#洗牌
items=[12,34,2,1,53,2,32]
random.shuffle(items)
print(items)

#生成随机验证码
chekcode=''
for i in range(5):
	current=random.randrange(0,5)
	if current != i:
		temp=chr(random.randint(65,90))
	else:
		temp=random.randint(0,9)
	chekcode+=str(temp)
print(chekcode)