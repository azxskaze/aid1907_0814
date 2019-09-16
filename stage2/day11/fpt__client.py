from socket import *
from threading import Thread
import sys,os
ADDR = ('127.0.0.1',8888)
class FtpClient:
    def __init__(self,connfd):
        self.connfd = connfd
    def do_list(self):
        self.connfd.send(b'L')
        data = self.connfd.recv(1024)
        if data == b'OK':

            data = self.connfd.recv(1024*1024).decode()
            print(data)
        else:
            print(data)
            print(111)
    def do_get(self,filename):
        print(filename)
        self.connfd.send(b'G '+filename.encode())
        data = self.connfd.recv(1024)
        if data == b'OK':
            f = open(filename,'wb')
            print(filename)
            while True:
                data = self.connfd.recv(1024)
                if data == '##':
                    break
                f.write(data)
                print('ok')
            f.close()
        else:
            print(data.decode())

    def do_put(self,filename):
        self.connfd.send(b'P '+filename.encode())
        data = self.connfd.recv(1024)
        if data == b'OK':
            f = open(filename,'rb')
            while True:
                data = f.read(1024)
                if not data:
                    self.connfd.send(b'##')
                    break
                self.connfd.send(data)
            f.close()
    def do_quit(self):
        self.connfd.send(b'Q')
        self.connfd.close()
        sys.exit()
def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except:
        return
    ftp = FtpClient(sockfd)
    while True:
        cmd = input('请输入选项：')
        # cmd = input("Command:")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.split(' ')[-1]
            ftp.do_put(filename)
        else:
            print("请输入正确命令!")
if __name__ == '__main__':

    main()






