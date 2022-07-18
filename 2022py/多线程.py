#！/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:xiaochao


'''

进程：进程是执行中的程序，拥有独立地址空间、内存、数据栈等
进程是由系统管理

线程：同进程下执行，并共享相同的上下文
线程间的信息共享和通信更加容易，多线程并行执行，需要同步原语

'''
import _thread
from time import sleep,ctime
import logging
logging.basicConfig(level=logging.INFO)

# loops=[2,4]
#
#
#
# def loop(nloop,nsec,lock):
# 	logging.info('stat loop'+str(nloop)+"at"+ctime())
# 	sleep(nsec)
# 	logging.info('end loop'+str(nloop)+"at"+ctime())
# 	lock.release()
# def main():
# 	logging.info('stat all at'+ctime())
# 	locks=[]
# 	nloops=range(len(loops))
# 	for i in nloops:
# 		lock=_thread.allocate_lock()#声明一个锁
# 		lock.acquire()#加锁
# 		locks.append(lock)
#
# 	for i in nloops:
# 		_thread.start_new_thread(loop,(i,loops[i],locks[i]))
# 	for i in nloops:
# 		while locks[i].locked():pass
#
# 	logging.info('end all at'+ctime())
# if __name__ == '__main__':
# 	main()

# import threading
#
# loops=[2,4]
#
#
#
# def loop(nloop,nsec):
# 	logging.info('stat loop'+ str(nloop) +" at"+ctime())
# 	sleep(nsec)
# 	logging.info('end loop'+ str(nloop) +" at"+ctime())
#
# def main():
# 	logging.info('stat all at'+ctime())
# 	nloops=range(len(loops))
#
# 	threads=[]
# 	for i in nloops:
# 		t=threading.Thread(target=loop,args=(i,loops[i]))
# 		threads.append(t)
# 	for i in nloops:
# 		threads[i].start()
# 	for i in nloops:
# 		threads[i].join()
# 	logging.info('end all at'+ctime())
# if __name__ == '__main__':
# 	main()

import threading
loops=[]
class MyThread(threading.Thread):
	def __init__(self,func,args,name=""):
		threading.Thread.__init__(self)
		self.func=func
		self.args=args
		self.name=name
	def run(self):
		self.func(*self.args)
def loop(nloop,nsec):
	logging.info('stat loop'+ str(nloop) +" at"+ctime())
	sleep(nsec)
	logging.info('end loop'+ str(nloop) +" at"+ctime())

def main():
	logging.info('stat all at'+ctime())
	nloops=range(len(loops))

	threads=[]
	for i in nloops:
		t=MyThread(loop,(i,loops[i]),loop.__name__)
		threads.append(t)
	for i in nloops:
		threads[i].start()
	for i in nloops:
		threads[i].join()
	logging.info('end all at'+ctime())
if __name__ == '__main__':
	main()