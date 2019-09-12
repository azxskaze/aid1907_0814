from socket import *
from gevent import monkey
import gevent
monkey.patch_all()
from socket import *
class Http:
    def __init__(self,addr,num,dict):
        self.dict = dict
        self.addr = addr
        self.num = num
    def fun(self,s):
        while True:
            c, addr = s.accept()
            data = c.recv(4096).decode()
            for k in self.dict:
                if data.split('\n')[0].split(' ')[1] == k:
                    f = open(self.dict[k],'r')
                    html1 = '''HTTP/1.1 200 OK
                            Content-Type:text/html

                            %s
                            ''' % f.read(1024)
                    f.close()
                    break
            else:
                html1 = '''HTTP/1.1 200 OK
                        Content-Type:text/html

                        <h1>sorry</h1>
                        '''
            c.send(html1.encode())
            c.close()
    def main(self):
        while True:
            s = socket()
            s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            s.bind(self.addr)

            s.listen(self.num)
            f = gevent.spawn(self.fun,s)
            gevent.joinall([f])
            # self.fun(s)


if __name__ == '__main__':
    dict1 = {'/':'/home/tarena/PycharmProjects/aid1907/stage2/day07/http练习/index.html'}
    h = Http(('0.0.0.0',12347),5,dict1)
    h.main()