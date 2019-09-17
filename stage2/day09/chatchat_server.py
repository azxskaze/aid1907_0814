'''
微信聊天室 udp
'''
from socket import *
import os,sys

HOST = '0.0.0.0'
POST = 1234
ADDR = (HOST,POST)
# 存储用户{name:address}
user = {}

def do_login(s,name,addr):
    if name in user or '管理员' in name:
        s.sendto('用户名已存在'.encode())
        return
    else:
        '''返回正确代码'''
        s.sendto(b'OK',addr)
        '''通知其他用户'''
        msg = '欢迎%s加入'%name
        for i in user:
            s.sendto(msg.encode(),user[i])
        user[name] = addr
def do_chat(s,name,text):
    if name in user:
        for i in user:
            if i != name:
                msg = '%s:%s'%(name,text)
                s.sendto(msg.encode(),user[i])
def do_quit(s,name):
    if name in user:
        s.sendto(b'EXIT',user[name])
        del user[name]
        for i in user:
            msg = '%s退出聊天室'%name
            s.sendto(msg.encode(),user[i])
# 循环接受客户端请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        tmp = data.decode().split(' ')
        print(tmp[0])
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr)
        elif tmp[0] == 'C':
            do_chat(s,tmp[1],' '.join(tmp[2:len(tmp)]))
        else:
            do_quit(s,tmp[1])
# 搭建网络
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    '''给管理员消息新创建进程'''
    pid = os.fork()
    if pid < 0:
        print('error')
    elif pid == 0:
        while True:
            msg = input('管理员消息：')
            msg = 'C 管理员 '+msg
            s.sendto(msg.encode(),ADDR)
    else:
        do_request(s)

if __name__ == '__main__':
    main()