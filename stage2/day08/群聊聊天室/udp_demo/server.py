from socket import *
import os
s1 = socket(AF_INET,SOCK_DGRAM)
s1.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s1.bind(('176.234.6.35',12345))
set_name = set()
set_addr = set()
def requst(s1):
    data,addr = s1.recvfrom(1024)
    if data in set_name:
        fasong()
def jinru(data,addr):
    if data in set_name:
        s1.sendto('名字重复'.encode(),addr)
        return False
    else:
        set_name.add(data.decode())
        set_addr.add(addr)
        return True

def tuichu():
    pass
def shou():
    data,addr = s1.recvfrom(1024)
    for i in set_addr:
        s1.sendto(data,i)








