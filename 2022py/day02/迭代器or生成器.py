#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao

#列表生成式
a=[1,2,3,4,5,6,7,8,9]
b=[]

for i in a:b.append(i+1)

print(a)
print(b)

for index,i in enumerate(a):
	a[index]+=1
	print('下标%s,列表中的元素%s'%(index,i))
print("a:",a)


a=map(lambda s:s+1,a)
for i in a:print(i)
print("xxxxx:",a)

s=[i+1 for i in range(10)]
print('s:',s)

#生成器
a1=[i+1 for i in range(10)]#创建list

a2=(i+1 for i in range(10))#创建generator
print(a1,a2)
#调用generator
for i in a2:
#print(next(a2)
	print(i)

#斐波拉契数列
# def fib(max):
# 	n,a,b=0,0,1
# 	while n<max:
# 		print(b)
# 		a,b=b,a+b
# 		n+=1
# 	return 'done'

def fib1(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n+=1
	return 'done'
s1=fib1(10)
print(s1)
print(s1.__next__())
print(s1.__next__())
print(s1.__next__())
print('ninhassss')
print(s1.__next__())


s22=fib1(100)
while True:
	try:
		x=next(s22)
		print('s22:',x)
	except StopIteration as e:
		print('x========',e.value)
		break
# for n in fib1(10):
# 	print(n)

#通过yield实现在单线程情况下实现并发运算效果
import time
def consumer(name):
	print('%s准备吃包子了'%name)
	while True:
		baozi=yield
		print('包子[%s]来了，被[%s]吃了！'%(baozi,name))

def producer(name):
	c=consumer('A')
	c2=consumer('B')
	c.__next__()
	c2.__next__()
	print('开始准备做包子了')
	for i in range(10):
		time.sleep(1)
		print('做了2个包子')
		c.send(i)
		c2.send(i)

producer('tom')