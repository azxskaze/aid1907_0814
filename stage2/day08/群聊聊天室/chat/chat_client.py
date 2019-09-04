'''chat room 客户端
    发送请求，展示结果'''
from socket import *
import signal
import os,sys
ADDR = ('176.234.6.35',1234)
def send_msg(s,name):
    while True:
        try:
            text = input('>>')
        except (KeyboardInterrupt,SyntaxError):
            text = 'quit'
        if text == 'quit':
            msg = 'Q '+name
            s.sendto(msg.encode(),ADDR)
            sys.exit('退出聊天室')
        msg = 'C %s %s'%(name,text)
        s.sendto(msg.encode(),ADDR)
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(4096)
        '''服务端有两个进程都需要退出'''
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode(),'\n>>')
# 搭建网络
def main():
    s = socket(AF_INET,SOCK_DGRAM)
# 进入聊天室
    while True:
        name = input('请输入昵称')
        msg = 'L ' +name
        s.sendto(msg.encode(),ADDR)
        data,addr = s.recvfrom(128)
        if data == b'OK':
            print('您已进入聊天室')
            break
        else:
            print(data.decode())

    pid = os.fork()
    if pid < 0:
        sys.exit('error')
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)
# 此时已经进入聊天室
if __name__ == '__main__':
    main()