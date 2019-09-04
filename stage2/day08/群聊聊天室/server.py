from socket import *
import os
s1 = socket()
s1.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s1.bind(('176.234.6.35',12345))
s1.listen(5)
set_name = set()
set_addr = set()
set_c = set()
def qunfa(set_c,str1):
    for i in set_c:
        i.send(str1.encode())
while True:
    c,addr = s1.accept()
    if c not in set_c:
        def jinruqunliao():
            while True:
                data = c.recv(1024).decode()
                if data in set_name:
                    n = c.send('名字重复，请重新输入'.encode())
                    continue
                else:
                    set_name.add(data)
                    set_addr.add(addr)
                    set_c.add(c)
                    break
            data = data+'进入群聊'
            qunfa(set_c,data)
    else:
        pid = os.fork()






