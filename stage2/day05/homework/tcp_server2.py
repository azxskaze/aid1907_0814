import socket

s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind(('0.0.0.0',12346))

s1.listen(5)
while True:
    print('waitting')
    connfd,addr = s1.accept()
    print('succeed connext:',addr)
    data = connfd.recv(1024)
    print('receive:',data.decode())
    n = connfd.send('thanks'.encode())
    print('send %d bytes' % n)
    connfd.close()
s1.close()