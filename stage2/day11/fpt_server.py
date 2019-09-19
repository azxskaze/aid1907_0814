from socket import *
from threading import Thread
import sys,os
from time import sleep

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
FTP = "/home/tarena/下载/" # 文件库位置

class FtpServer(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()
    def do_list(self):
        files = os.listdir(FTP)
        if not files:
            print('no')
            self.connfd.send('打钱'.encode())
            return
        else:

            self.connfd.send(b'OK')
            sleep(0.1)
        filelist = ''
        for file in files:
            if file[0] != '.'\
                    and os.path.isfile(FTP+file):
                filelist += file + '\n'

        self.connfd.send(filelist.encode())
    def do_get(self,filename):
        try:
            print(filename)
            f = open(FTP+filename,'rb')
        except :
            self.connfd.send('打钱'.encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        f.close()
    def do_put(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send('已存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
        f = open(FTP+filename,'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
            f.close()
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == 'Q':
                sys.exit()
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    while True:
        try:
            c,addr = s.accept()
        except:
            continue
        t = FtpServer(c)
        t.daemon = True
        t.start()
if __name__ == '__main__':
    main()