import socket

s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind(('0.0.0.0',2346))
f=open('2.txt','wb')
s1.listen(5)

print('waitting')
connfd,addr = s1.accept()
print('succeed connext:',addr)
data = connfd.recv(102400)
# print('receive:',data.decode())
f.write(data)
n = connfd.send('thanks'.encode())
print('send %d bytes' % n)
connfd.close()
f.close()
s1.close()