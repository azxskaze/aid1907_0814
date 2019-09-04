'''tcp_client.py  tcp套接字客户端流程
    重点代码，要和服务端配合，使用同样的套接字类型'''
import socket

# s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1 = socket.socket()
# 创建tcp套接字
server_addr=('176.234.6.35',2346)

'''recv也是阻塞函数'''

s1.connect(server_addr)
f = open('/home/tarena/桌面/购物.txt','rb')

'''要和服务端错开，先发后收'''

    # s1.send(input('发送：').encode())
s1.send(f.read())
key = s1.recv(1024).decode()

s1.close()