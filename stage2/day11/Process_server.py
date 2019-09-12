from multiprocessing import Process
from socket import *
import os
import signal
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
# 全局变量
HOST = '127.0.0.1'
PORT = 8889
ADDR = (HOST,PORT)
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()


while True:
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(('0.0.0.0',1234))
    s.listen(5)
    # 处理僵尸进程
    print("Listen the port 8888...")
    c,addr = s.accept()
    p = Process(target=handle,args=(c,))
    p.daemon=True
    p.start()
