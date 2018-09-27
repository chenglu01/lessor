# -*-code: utf-8-*-
import os
print 'Process (%s) start ...' % os.getpid()
pid = os.fork()
if pid == 0:
    print 'I am (%s) childprocess my parent is %s' % (os.getpid(),os.getppid())
else:
    print 'I (%s) just created (%s)' % (os.getpid(),pid)
