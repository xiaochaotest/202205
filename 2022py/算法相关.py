#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

#
#斐波拉契数列
# def fib(max):
# 	n,a,b=0,0,1
# 	while n<max:
# 		print(b)
# 		a,b=b,a+b
# 		n+=1
# 	return 'done'
def s1(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n+=1
	return 'deom'
#冒泡排序
data=[1,34,23,12,45,22,2]
print('list=',data)

previous=data[0]
for j in range(len(data)):
	tmp=0
	for i in range(len(data)-1):
		if data[i] > data[i+1]:
			tmp=data[i]
			data[i]=data[i+1]
			data[i+1]=tmp
	#print(data)

print('排序后：',data)

#生成一个4*4的2维数组并将其顺时针旋转90度
