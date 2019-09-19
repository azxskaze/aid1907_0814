import socket
import pymysql
import sys
from threading import Thread
ADDR = ('0.0.0.0',12345)

class DictServer(Thread):
    def __init__(self,connfd):
        self.s = connfd
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='dict1',
                                  charset='utf8')
        self.cur = self.db.cursor()
        super().__init__()

    def login(self,list1):
        print('login')
        sql = "select usr from user where usr=%s;"
        self.cur.execute(sql, list1[0])
        data = self.cur.fetchone()
        print(data)
        if data:
            self.s.send(b'NO')
            return False
        sql1 = "insert into user values (%s,%s);"
        try:
            self.cur.execute(sql1, list1)
            self.db.commit()
            self.s.send(b'OK')
            print('loginok')
            return True
        except:
            self.s.send(b'ERRO')
            print('loginno')
            self.db.rollback()
    def delete(self,list1):
        print('delete')
        sql = "select * from user where usr=%s and password=%s;"
        self.cur.execute(sql, list1)
        data = self.cur.fetchone()
        print(data)
        if data:
            sql = "delete from user where usr=%s and password=%s"
            try:
                self.cur.execute(sql,list1)
                self.s.send(b'OK')
                self.db.commit()
            except:
                self.s.send(b'NO')
                self.db.rollback()
        else:
            self.s.send(b'NO')
    def logon(self,list1):
        print('logon')
        print(list1)
        sql = "select * from user where usr=%s and password=%s;"
        self.cur.execute(sql,list1)
        data = self.cur.fetchone()
        print(data)
        if data:
            print('logonok')
            self.s.send(b'OK')
            return True
        else:
            self.s.send(b'NO')
            print('loginno')

    def do_dict(self,list1):
        print('dict')
        sql = "select mean from words where word=%s"
        self.cur.execute(sql,list1[1])
        mean = self.cur.fetchone()
        if mean:
            self.s.send(b'OK')
            self.do_note(list1)
            list1 = list(mean)
            str1 = '*'.join(list1)
            self.s.send(str1.encode())
        else:
            self.s.send(b'NO')
    def do_note(self,list1):
        sql = "insert into history (name,word) values (%s,%s)"
        try:
            self.cur.execute(sql,list1)
            self.db.commit()
        except:
            self.db.rollback()
    def do_history(self,list1):
        print('history')
        sql = "select * from history where name=%s"
        self.cur.execute(sql,list1[0])
        data = self.cur.fetchmany(10)
        if data:
            self.s.send(b'OK')
            list1 = list(data)
            str1 = ''
            for i in list1:
                str1 += '*'+str(i)
            self.s.send(str1.encode())
        else:
            self.s.send(b'NO')

    def run(self):
        while True:
            data = self.s.recv(1024).decode()
            list1 = data.split(' ')
            key = list1[0]
            m = list1[1:3]
            print(m)
            if key == 'IN':
                self.login(m)
            elif key == 'ON':
                self.logon(m)
            elif key == 'D':
                self.do_dict(m)
            elif key == 'H':
                self.do_history(m)
            elif key == 'Q':
                sys.exit()
            elif key == 'DE':
                self.delete(m)

def main():
    s = socket.socket()
    s.bind(ADDR)
    s.listen(3)
    while True:
        try:
            c,addr = s.accept()
        except:
            continue
        t = DictServer(c)
        t.daemon = True
        t.start()
if __name__ == '__main__':
    main()