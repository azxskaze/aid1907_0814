'''udp客户端'''
import socket
ADDR = ('176.234.6.35', 12345)
# 数据包套接字（有边界的包）
s1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    DATA=input('发送')
    if not DATA:
        break
    s1.sendto(DATA.encode(), ADDR)
    data,addr=s1.recvfrom(30)
    print(data.decode())
s1.close()