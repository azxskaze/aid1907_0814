'''udp套接字服务端
    udp服务端不需要对客户端的状态进行判断
    有人请求就回应，没有请求就什么也不做
    （无连接协议）

    UDP不会粘包，但是会丢包，超出接收大小的部分会直接丢弃
    '''
import struct
import socket
s1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s1.bind(('0.0.0.0',12345))
st=struct.Struct('i16sif')
f = open('student.txt','w')
while True:
    data,addr = s1.recvfrom(1024)
    if not data:
        break
    student=st.unpack(data)
    f.write((str(student[0])))
    f.write('%-10s'%student[1].decode().strip(b'\x00'.decode()))
    print('%10s'%student[1].decode())
    f.write(str(student[2]))
    f.write(str(student[3]))
    f.write('\n')


    # print(student)
    # f.writelines('%d  %-10s.decode() %d %.1f'%student)


s1.close()
