#! -*- coding:utf-8 -*-
import gevent
from gevent import monkey;monkey.patch_all()
import urllib2
def get_body(i):
	print "start",i
	urllib2.urlopen("http://cn.bing.com")
	print "end",i
tasks=[gevent.spawn(get_body,i) for i in range(50)]
gevent.joinall(tasks)
