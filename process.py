#!-*- coding: utf-8 -*-
import threading
from time import ctime,sleep
def music(func):
    for i in range(2):
        print 'i was listen to a music %s %s\n' % (func,ctime())
        sleep(20)
def movie(func):
    for i in range(2):
        print 'i was watch the movie %s ,%s' % (func,ctime())
        sleep(25)

threads = []

t1 = threading.Thread(target=music,args=(u'矮胖',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=(u'激战',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    print 'all over at %s' % ctime()
