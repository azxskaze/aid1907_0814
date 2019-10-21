#!/usr/bin/env python3

'''
获取http请求
解析http请求
将请求发送给WebFrame(使用json)
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
'''

import json
from socket import *
import sys
from threading import Thread
import re
from config import *

#和frame进行交互
def connect_frame(env):
    s = socket()
    try:
        # 链接webframe
        s.connect((frame_ip,frame_port))
    except:
        return
    data = json.dumps(env)
    #转换为json格式
    s.send(data.encode())
    data = s.recv(1024*1024).decode()
    #从json格式转化为python数据类型
    print(type(data),data)
    try:
        return json.loads(data)
    except:
        return

# return json.loads(data) #{'status':200,'data':'ccc'}

class HTTpServer():
    def __init__(self):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.create_socket()
        self.bind()

    def create_socket(self):

        self.socked = socket()
        self.socked.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)

    def bind(self):

        self.socked.bind(self.address)

    def server_forever(self):

        self.socked.listen(5)
        print('listen the port %d'%self.port)
        while True:
            connfd,addr = self.socked.accept()
            client = Thread(target = self.handle,
                            args = (connfd,))
            client.setDaemon(True)
            client.start()

    def handle(self,connfd):

        request = connfd.recv(4096).decode()
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern,request).groupdict()
            #match 只匹配开头
        except:
            connfd.close()
            return
        else:
            response = connect_frame(env)#向后台程序转发请求并接受结果
            if response:
                self.send_response(connfd,response)
    # 组织http响应,发送给浏览器
    def send_response(self,connfd,response):
        # {'status':200,'data':'ccc'}
        print(type(response['status']))
        print(response['status'])
        if response['status'] == '200':
            data1 = "HTTP/1.1 200 OK\r\n"
            data1 += "Content-Type:text/html\r\n"
            data1 += "\r\n"
            data1 += response['data']

        elif response['status'] == '404':
            data1 = "HTTP/1.1 404 NOT Found\r\n"
            data1 += "Content-Type:text/html\r\n"
            data1 += "\r\n"
            data1 += response['data']
        elif response['status'] == '500':
            data1 = "HTTP/1.1 500 smile\r\n"
            data1 += "Content-Type:text/html\r\n"
            data1 += "\r\n"
            data1 += response['data']

        connfd.send(data1.encode())
        # print(data)


if __name__ == '__main__':

    http = HTTpServer()
    http.server_forever()#启动服务