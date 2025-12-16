#! -*- coding:utf-8 -*-
from multiprocessing import Process as pro
from multiprocessing.dummy import Process as thr
from gevent import monkey;monkey.patch_all()
import gevent
def run(i):
	lists=range(i)
	list(set(lists))
	
if __name__=="__main__":
	'''
	多进程
	'''
	#for i in range(30):      ##10-2.1s 20-3.8s 30-5.9s
	#	t=pro(target=run,args=(5000000,))
	#	t.start()
	'''
	多线程
	'''
	for i in range(30):    ##10-3.8s  20-7.6s  30-11.4s
		t=thr(target=run,args=(5000000,))
	 	t.start()
	'''
	协程
	'''
	# jobs=[gevent.spawn(run,5000000) for i in range(30)]  ##10-4.0s 20-7.7s 30-11.5s
	# gevent.joinall(jobs)
	# for i in jobs:
	# 	i.join()
