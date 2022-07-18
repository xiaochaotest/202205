#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

'''
str

'''
name1 = 'xiaochao,"你好"，\'你在成都好吗？\''
print(name1)

name = 'alix'
age  = 12
job = 20000
salary = 20000
#格式化輸出
info1 = '''
-------info of {_name}-----
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
'''.format(_name=name,_age=age,_job=job,_salary=salary)
#print(info1)
# '''字符串和unicode类型互转'''
str1  = 'hello word!'
print('查看类型：',type(str1))

# print u'str3的类型是：',type(str3)
# ''#将字符串转成int类src = '45'
# src1 = int(src)#浮点类型float(src)
# print ('将字符串强转为int类型：',type(src1))
#
#
name = 'my\tname is {name} and i am {age} old'.format(name=name,age=age)
# #首字母大写
print(name.capitalize())
# #统计字符串中出现的数量
print(name.count('m'))
# #打印10个-，并且将内容居中
print(name.center(10,'-'))
# #将二进制转成字符串
# print(name.encode())
# #判断一个字符串以什么结尾
# print(name.endswith('o'))
print(name.endswith('o'))
#
# name1 = 'my \tname is xiaochao'
# #输入\t(tab键)将tab键输入多少个间隔
print(name.expandtabs(tabsize=10))
print(name.expandtabs(tabsize=20))
# #查找字符串中的字符索引
# print(name.find('y'))
# #字符串切片
print('切片',name[name.find('name'):])
# #字符串格式化输出
# print(name.format(name = 'xiaochao',age = 24))
# #阿拉伯数字+字母
print(name.isalnum())
# #判断是否为纯英文字符
# print('sas1'.isalpha())
# #是否是整数
# print('22'.isdigit())
# #判断是不是一个合法的标识符
# print('A艾大df1'.isidentifier())
# #判断是不是小写
# print('set'.lslower())
# #判断是不是一个纯数字
# print('res1'.isnumeric())
# #判断是不是空格
# print('sd2'.isspace())
# #判断每个首字母是否大写
# print('my Name is'.istitle())
# #大小写转换
# print('das'.swapcase())
# #判断是不是大写
# print('das'.isupper())
# #将列表以，拼接
# print(','.join(['1','2','3']))
# #字符串长度不够10就用*号向后补齐
# print(name.ljust(10,'*'))
print('字符串长度不够10就用*号向后补齐',name.ljust(50,'#'))
# #字符串长度不够10就用-号向前补齐
# print(name.rjust(10,'-'))

# #首字母小写
# print('Sr'.lower())
# #左边有空格或者回车去掉输出
# print('\nAstr'.lstrip())
# #右边有空格或者回车会去掉输出
# print('Astn\n'.rstrip())
# #去掉空格或回车
# print('  dasnt\n'.strip())
# #小写转为大写
# print('dfa'.upper())
# #根据后面的字母找到对应的数字
# p = name.maketrans('abcderf1','12345566')
# print('xiaochao'.translate(p))
# #替换
# print('sdw'.replace('s','A'))
# #找到最右边一个值得下标
# print('xiaochao'.rfind('a'))
# #将字符串以空格拆分成列表
# print('xiao chao'.split(' '))
# #以换行拆分
# print('xiao\nchao'.splitlines())
#
#
# '''字符串的操作'''
# cont = 'hell word'
# print u'获取w在字符串中是第几位：',cont.index('w')#索引均是从0开始
# print cont.index('l')
# print u'取消字符串中的空格：',cont.strip()
# cont.strip()
# print u'判断字符串是否是数字：',cont.isdigit()
# cont.isdigit()
# print u'寻找字符串中的元素：',cont.find('o')
# cont.find('s')
# print u'替换字符串中的元素：',cont.replace('word','China')
# cont.replace('word','name')
# print u'字符串的拆分：',cont.split(' ')#字符串拆分处理以后就是列表
# cont.split(' ')
# print u'首字母变大写：',cont.capitalize()
# cont.capitalize()
# print u'内容居中：',cont.center(30,'=')
# #cont.center(30,'==')
# cont1 = 'Hello\t999'
# print u'处理table键：',cont1.expandtabs()
# print u'是否是字母和数字：',cont.isalnum()
# print u'是否是字母：',cont.isalpha()
# print u'判断是否是数字：',cont.isdigit()
# print u'是否小写：',cont.islower()
# print u'是否有空格：',cont.isspace()
# print u'是否是大写：',cont.isupper()
# #判断标题-->首字母大写，可以理解为大写
# print u'首字母是否大写:',cont.istitle()
# #join连接字符串
# s1 = ['appium','selenium','android','ios']
# print '连接字符串:', '***'.join(s1)
# #使用.join（）把列表转为字符串
# print '把列表转成字符串：',','.join(s1)
# #字符串转为列表
# a = 'a b c'
# print a.split(" ")
# #移除空白
# a1 = '  abc'
# print '移除空白:',a1.lstrip()
# #移除左侧空白
# print '移除左侧空白：',a1.lstrip()
# #移除右侧空白
# st = 'hell   '
# print '移除右侧空白：',st.rstrip()
# #字符串转小写
# print cont.lower()
# #分割字符串，分割之后就是元组
# ss1 = 'xiaochao is python'
# print u'分割字符串，分割之后就是元组：',ss1.partition('is')
# #替换字符串
# print u'替换字符串：',ss1.replace("xiaochao",'admin')
# #rfind()从右向左找
# print ss1.find('xiaochao')
#
# #ytes可以将字符串转换成字节
# strs1 = u'小超'
# print u'字符串转成字节：',strs1.bytes(strs1)

'''
while
'''
w_age=22
count=0
while count<3:
	age=int(input('你的年齡：'))
	if age==w_age:
		print('caiduil')
		break
	elif age>w_age:
		print('大了')
	else:
		print('小了')
	count+=1
else:
	print('caidecishutaiduole')


# age_of_oldboy = 56
#
# count = 0
# while count <3:
#     guess_age = int(input("guess age:") )
#     if guess_age == age_of_oldboy :
#         print("yes, you got it. ")
#         break
#     elif guess_age > age_of_oldboy:
#         print("think smaller...")
#     else:
#         print("think bigger!")
#     count +=1
# else:
#     print("you have tried too many times..fuck off")

#输出3次python
count = 0
while count < 3:
	print('python')
	count +=1
#计算1-100累计和
i = 0
result =0
# while i <=100:
# 	result+=i
# 	i+=1
# print(result)

#计算偶数和
# while i<=100:
# 	if i % 2 ==0:
# 		result+=i
# 	i+=1
# print(result)
#打印乘法表

row = 1
while row <= 9:
	col = 1
	while col <= row:
		print ('%d * %d = %d\t' % (col,row, col*row),end=''),
		col += 1
	# print '%d' % row
	print()
	row += 1


row=0
while row<=9:
	col=1
	while col<=row:
		print('%d*%d=%d\t'%(col,row,col*row),end='')
		col+=1

	print()
	row+=1



'''
for
'''
# age_of_oldboy1 = 56
#
# for i in range(3):
#     guess_age = int(input("guess age:") )
#     if guess_age == age_of_oldboy1 :
#         print("yes, you got it. ")
#         break
#     elif guess_age > age_of_oldboy1:
#         print("think smaller...")
#     else:
#         print("think bigger!")
# else:
#     print("you have tried too many times..fuck off")