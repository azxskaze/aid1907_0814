'''select tcp'''
from socket import *
from select import select

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

rlist = [s]
wlist = []
xlist = []
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for i in rlist:
        if i == s:
            c,addr = i.accept()
            rlist.append(c)
        else:
            data = i.recv(1024)
            if not data:
                rlist.remove(i)
                i.close()
                continue
            print(data.decode())
            wlist.append(i)
    for r in wlist:
        r.send(b'OK')
        wlist.remove(r)
