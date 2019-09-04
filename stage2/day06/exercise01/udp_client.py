'''udp客户端'''
import socket
import struct
ADDR = ('176.234.6.35', 12345)
# 数据包套接字（有边界的包）
s1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
st=struct.Struct('i16sif')

while True:
    id=int(input('id'))
    name=input('姓名')
    age=int(input('年龄'))
    score=float(input('成绩'))
    data = st.pack(id,name.encode(),age,score)
    print(type(data))
    s1.sendto(data, ADDR)
    # print(data.decode())
s1.close()