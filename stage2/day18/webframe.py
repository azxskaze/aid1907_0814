#!/usr/bin/env python3
# ./文件名 &
# kill -9 39305
from socket import *
import json
import settings
from settings import *
from multiprocessing import Process
from urls import *

class Application:
    def __init__(self):
        self.host = app_host
        self.port = app_port
        self.address = (self.host,self.port)
        self.create_sockfd()
        self.bind()
    def create_sockfd(self):
        self.socked = socket()
        self.socked.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
    def bind(self):
        self.socked.bind((self.address))
    def send_html(self,info):
        print(info)
        if info == '/':
            filename = 'index.html'
        else:
            filename = info
        try:
            f = open('static/' + filename,'r')
        except:

            d = open('static/4041.html')
            data =d.read()
            status = '404'
        else:
            data = f.read()
            status = '200'

        finally:
            return {'status':status,'data':data}

    # def send_data(self,connfd):
    #     f = open('static/Xmind.jpg','rb')
    #     status = '500'
    #     data = f.read()
    #
    #     message = json.dumps({'status':status,'data':data.decode()})
    #     print(type(message),message)
    #     connfd.send(message)

    def server(self,connfd):
        data = connfd.recv(4096).decode()
        data = json.loads(data.encode())
        print(data)
        if data['method'] == 'GET':
            if data['info'] == '/' or data['info'][-5:] == '.html':
                message = self.send_html(data['info'])
            else:
                message = self.get_data(data['info'])
                # self.send_data(connfd)
            connfd.send(json.dumps(message).encode())

    def main(self):
        self.socked.listen(5)
        while True:
            connfd,addr = self.socked.accept()
            p = Process(target = self.server,kwargs={'connfd':connfd})
            p.daemon = True
            p.start()
    def get_data(self,info):
        for url,func in urls:
            if url == info:
                return {'status':'200','data':func()}
        else:
            return {'status':'404','data':'sorry'}
if __name__ == '__main__':
    app = Application()
    app.main()
