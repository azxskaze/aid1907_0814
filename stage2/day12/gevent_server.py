'''基于协程的tcp并发'''
from gevent import monkey
import gevent
monkey.patch_all()
# 让普通阻塞变成协程阻塞
from socket import *

def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            return
        print(data)
        c.send(b'OK')
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',1234))
s.listen(5)
i=1
while True:
    print(i,'**')
    i+=1
    c,addr = s.accept()
    print('from:',addr)
    # handle(c) #循环方案
    gevent.spawn(handle,c) #写成协程

