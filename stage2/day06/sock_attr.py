'''套接字属性'''
import  socket
s1 = socket.socket()
s1.bind(('0.0.0.0',11111))
s1.listen(5)
c,d=s1.accept()
print(dir(s1))
print('地址类型：',s1.family)
print('套接字类型：',s1.type)
print('绑定地址：',s1.getsockname())
print('文件描述符：',s1.fileno())
# print('获取连接端地址：',链接套接字（实际）.getpeername())只有有链接的时候才能使用
print('套接字类型：',c.getpeername())


