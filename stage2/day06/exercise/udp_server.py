'''udp套接字服务端
    udp服务端不需要对客户端的状态进行判断
    有人请求就回应，没有请求就什么也不做
    （无连接协议）

    UDP不会粘包，但是会丢包，超出接收大小的部分会直接丢弃
    '''
import socket
s1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s1.bind(('0.0.0.0',12346))
f = open('dict.txt','r')

while True:
    data,addr = s1.recvfrom(300)
    if not data:
        break
    print('message from %s:%s'%(addr,data.decode()))
    for line in f:
        list1=line.split(' ')
        if data.decode() == list1[0]:
            jieguo=' '.join(list1[1:-1]).strip()
            print(jieguo)
    s1.sendto(jieguo.encode(),addr)
s1.close()
