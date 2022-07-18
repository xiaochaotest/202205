#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao
#用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
import hashlib

#md5加密
m=hashlib.md5()
m.update(b'hello')
m.update(b'It`s me')
print(m.digest())#输出二进制hash
print(m.hexdigest())#输出16进制hash
m.update(b'It~ been along time since last time we...')

ma=hashlib.md5()
ma.update(b'hello It`s me')
print(ma.hexdigest())


m1=hashlib.sha1()
m1.update(b'hello It`s me')
print(m1.hexdigest())

m2=hashlib.sha256()
m2.update(b'hello It`s me')
print(m2.hexdigest())

m3=hashlib.sha384()
m3.update(b'hello It`s me')
print(m3.hexdigest())

m4=hashlib.sha512()
m4.update(b'hello It`s me')
print(m4.hexdigest())

#主要用于消息加密
import hmac #它内部对我们创建的key和内容在进行处理然后加密

h = hmac.new(b'12323423',b'23423')
#h.update('hello')
print(h.hexdigest())#16进制
print(h.digest())#10进制
