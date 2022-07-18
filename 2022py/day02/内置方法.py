#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

print(all([1, 9,]))#非0为真
print(any([]))

print(bin(10))#把数字十进制转为二进制

print(bool(1))

a=bytes('ser1', encoding='utf-8')
b=bytearray('srce1', encoding='utf-8')
print(a)
print(b)#把二进制改成列表格式，就可以对其修改
print(b[1])