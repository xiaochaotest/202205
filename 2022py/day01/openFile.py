#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

'''
1.打开文件，得到文件句柄并赋值给一个变量
2.通过句柄对文件进行操作
3.关闭文件

打开文件的模式有：

r，只读模式（默认）。
w，只写模式。【不可读；不存在则创建；存在则删除内容；】
a，追加模式。【可读；   不存在则创建；存在则只追加内容；】
"+" 表示可以同时读写某个文件

r+，可读写文件。【可读；可写；可追加】
w+，写读
a+，同a
"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）

rU
r+U
"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）

rb
wb
ab
'''
import os,sys
#读整个文件
f=open("yestdays",'r',encoding='utf-8')#文件句柄
# data=f.read()

# print(data)
print('----------------')
#读一行
# data1=f.readline()
# data2=f.readlines()#效率不高可读小文件
# print("读一行：",data1)
# print(data2)
# print('写'.center(20,'-'))
# f1=open("写入创建的文件",'w',encoding='utf-8')#文件句柄
# f1.write('nihaohaohaooho,\n')
# f1.write('杭浓弄懂弄')
# f1.close()




# count = 0
# for line in f:
# 	count += 1
# 	if count == 9 :
# 		print('-------')
# 		continue
# 	print(line)
#
#
# print(f.tell())#打印当前位置
# print(f.seek(10))#回到指定位置
# print(f.readline())

s = open('yestdays','r',encoding='utf-8')
s1 = open('yestdays.bat','w',encoding='utf-8')

for line in s :
	if "我尝到了舌尖泪水的苦涩滋味" in line:
		line = line.replace("我尝到了舌尖泪水的苦涩滋味","张三尝到了舌尖泪水的苦涩滋味")
		s1.write(line)
s.close()
s1.close()