'''
tcp_server.py
tcp套接字服务端流程
重点代码
功能性代码，注重流程和函数使用
'''
import socket
# 第一步，创建一个tcp套接字(ipv4,tcp流式套接字)
# 流式套接字，没有消息边界，可能会粘包
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址（0.0.0.0或者本地ip其他主机也可以访问到，而172.0.0.1只能本地测试）
s1.bind(('0.0.0.0',12341))

# 设置监听(整数参数)
s1.listen(5)

# 等待处理客户端链接请求
print('waitting')
# connfd,为给此客户端建立的服务员，addr为此客户端的地址
connfd,addr = s1.accept()

print('succeed connext:',addr)

# 消息收发
# 收
data = connfd.recv(1)
print('receive:',data.decode())

# 发
# send()返回值为发送信息的字节数
n = connfd.send('thanks'.encode())
print('send %d bytes'%n)

# 关闭套接字
connfd.close()
s1.close()