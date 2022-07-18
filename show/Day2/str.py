#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:pc

str='admin'

print(str.replace('a', 'what'))#替换
print(str.startswith('a'))
print(str.endswith('n'))
print(str.isdigit())#判断是否是数字


#列表
list1=[1.25,23,1,2,12,15,32,5,156]
print(dir(list))

list1.append(222)#追加
list1.insert(0,112)#插入

print(list1)

print([x + 1 for x in list1 if x>20])#列表推导式



#元组
tuple1=(1,2,4,5,['wang',12],{"name":"zhangsan","age":22})

tuple1[4][0]='miaomiao'
print(tuple1)

tuple1[5]['name']='你好'
print(tuple1)


#字典
dict1={'name':'zhansan','age':12}
dict2=dict1.copy()
print(dict2)

print(dict1.get('age'))

for i,j in dict1.items():
	print(i,j)

for value in dict1.values():
	print(value)


dect3={"salary":8000}
dict1.update(dect3)
print(dict1)
print(dect3)

print(sorted(dict1.items(), key=lambda item: item[0]))#根据aci码进行排序

