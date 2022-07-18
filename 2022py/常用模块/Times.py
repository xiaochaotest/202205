#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

import time
#时间加减
import datetime
#从1970到现在的时间，s
print(time.time())

#返回处理时间
print(time.process_time())#0.5625
#返回与tuc的时间差,s
print(time.altzone)#-3240
#返回时间格式
print(time.asctime())#Mon Apr 11 15:08:55 2022
print('ctim:',time.ctime())
#返回本地时间，结果为UTC+8时区
print(time.localtime())#time.struct_time(tm_year=2022, tm_mon=4, tm_mday=11, tm_hour=15, tm_min=8, tm_sec=55, tm_wday=0, tm_yday=101, tm_isdst=0)
#返回utc时间的struc时间对象格式
print(time.time() - 800000)#1648861010.6318812
print(time.ctime())
#结果为utc时区
print('gm：',time.gmtime())

#日期字符串转成时间戳
strTime=time.strptime('2022/04/11','%Y/%m/%d')
print(strTime)
str1Time=time.mktime(strTime)
print('STR:',str1Time)#STR: 1649606400.0

#将时间戳格式转为日期字符串格式
t=time.strftime('%Y-%m-%d %H:%M:%S')
print('strftime:',time.strftime('%Y-%m-%d %H:%M:%S'))
#将日期字符串格式转为时间戳格式
print('时间戳格式：',time.strptime(t, '%Y-%m-%d %H:%M:%S'))


#时间加减
#获取当前时间
print(datetime.datetime.now())
#时间戳转换为日期2022-04-11
print(datetime.date.fromtimestamp(time.time()))
#当前时间+3天2022-04-14 15:30:54.307827
print(datetime.datetime.now() + datetime.timedelta(3))
#当前时间减三天2022-04-08 15:31:40.989247
print(datetime.datetime.now() + datetime.timedelta(-3))
#当前时间加3小时2022-04-11 18:32:21.621580
print(datetime.datetime.now() + datetime.timedelta(hours=3))
#当前时间加30分钟
print(datetime.datetime.now() + datetime.timedelta(minutes=30))
