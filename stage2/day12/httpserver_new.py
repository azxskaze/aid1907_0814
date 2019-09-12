from socket import *
from select import select

class HttpServer:
    def __init__(self,s,dir):

        self.dir = dir
        self.address = ('0.0.0.0',s)
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.main()
        self.bind()

    def main(self):
        self.s = socket()
        self.s.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR,
                               1)

    def bind(self):
        self.s.bind(('0.0.0.0',1238))


    def sendto(self,c1):
        request = c1.recv(4096)
        print(request)
        if not request:
            self.rlist.remove(c1)
            return
        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        print(info)
        if info == '/' or info[-5:] == '.html':
            self.send_html(c1,info)
        else:
            self.send_data(c1)
    def send_html(self,c,info):
        if info == '/':
            filename = self.dir+'index.html'
        else:
            filename = self.dir+info
        try:
            print(filename)
            f = open(filename)
        except Exception:
            text = 'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n'
        else:
            text = 'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n'+f.read()
        finally:
            c.send(text.encode())

    def send_data(self,c):
        filename=self.dir+'/Xmind.jpeg'
        print(filename)
        f = open(filename,'rb')
        text = 'HTTP/1.1 200 OK\r\nContent-Type:image/jpeg\r\n\r\n'.encode() + f.read()
        c.send(text)

    def handel(self):
        self.s.listen(3)
        self.rlist.append(self.s)
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.s:
                    c,addr = r.accept()
                    self.rlist.append(c)
                else:
                    self.sendto(r)

if __name__ == '__main__':
    ADDR = '0.0.0.0'
    S = 1237
    DIR = '/home/tarena/学习笔记/第二阶段/ddd'
    h = HttpServer(S,DIR)
    h.handel()