#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

import re
#从头匹配
#re.match(pattern=,string=)
a=re.match("[0-9]","2ale1ranin2jack3helen")
print(a)
#匹配这个字符串，知道找到一个匹配
#re.search(pattern=,string=)

#将匹配的格式当做分隔点对字符串分割成列表
#re.split()
q=re.split("^[0-9]","2ale1ranin2jack3helen")
print(q)

#找到所有要匹配的字符并返回列表格式
q1=re.findall("^[0-9]","2ale1ranin2jack3helen")
print('q1:',q1)

#替换匹配的字符
q2=re.sub('[0-9]','|','alex1rean2jsck3atom',count=2)
print('q2:',q2)


p = re.compile('^[0-9]')#生成匹配的正则对象，^代表开头匹配，【0-9】表示匹配0-9的任意数字
m=p.match('12324njlo342')#按上面生成的正则对象，去匹配字符串，如果匹配成功m就会有值
print(m.group())#返回匹配上的结果，此处为1


#常见例子
#匹配手机号
phone_str = "hey my name is alex, and my phone number is 13651054607, please call me if you are pretty!"
phone_str2 = "hey my name is alex, and my phone number is 18651054604, please call me if you are pretty!"

m = re.search("(1)([358]\d{9})", phone_str2)
if m:
	print(m.group())

#匹配IP V4
ip_addr = "inet 192.168.60.223 netmask 0xffffff00 broadcast 192.168.60.255"

m = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip_addr)

print(m.group())

#匹配email
email = "alex.li@126.com   http://www.oldboyedu.com"

m = re.search(r"[0-9.a-z]{0,26}@[0-9.a-z]{0,20}.[0-9a-z]{0,8}", email)
print(m.group())