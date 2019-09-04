'''只有当管道破裂（服务中断）
的时候才能发送空字符串
加sleep(0.1)可以有效解决粘包问题
'''
import socket

s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind(('0.0.0.0',12345))

s1.listen(5)
connfd,addr = s1.accept()
print('waitting')
while True:
    print('succeed connext:',addr)

    while True:
        data = connfd.recv(1024)
        print(data.decode())
        if data:
            print('receive:',data.decode())
            n = connfd.send('thanks'.encode())
            print('send %d bytes' % n)
        else:
            connfd.send(b'')
            break
            connfd.close()
s1.close()