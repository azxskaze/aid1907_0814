'''epoll方法实现IO多路复用
步骤：
1.创建套接字
2.将套接字register
3. 创建查找字典，并维护
4. 循环监控IO发生
5. 处理发生的IO
'''
from socket import *
from select import *

# 创建套接字作为关注IO
s = socket()
# tcp套接字

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',1234))
s.listen(3)

# 创建epoll对象
p = epoll()

# 建立查找字典，通过IO对象的fileno找到对象
# 字典内容与关注IO保持一致{s.fileno:io_obj}
fdmap = {s.fileno():s}

# 关注s
p.register(s,EPOLLIN|EPOLLERR)

# 循环监控IO的发生
while True:
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr =  fdmap[fd].accept()
            print('connect from:',addr)
            # 添加新的关注对象，同时维护字典
            p.register(c,EPOLLIN)
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024).decode()
            if data == '':
                print('*********')
                # 表示客户端退出
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                print(1)
                continue
            print(data)
            print(fdmap)
            # p.register(fd,EPOLLOUT)

        elif event & EPOLLOUT:
            fdmap[fd].send(b'OK')

