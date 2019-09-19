import socket
import hashlib
import pymysql
from threading import Thread
ADDR = ('0.0.0.0', 12345)
class Dict_client:
    def __init__(self,c):
        self.c = c
    def send1(self,message):
        self.c.send(message.encode())
        data = self.c.recv(1024)
        if data == b'OK':
            print('ok')
            return True
        print('no')
        return False
    def recv1(self):
        data = self.c.recv(1024)
        if data:
            return self.show(data.decode())
        else:
            return False
    def show(self,data):
        str1 = data.split('*')
        for i in str1:
            print(i)

def dict(user,c):
    word = input('输入要查询的单词：')
    message = 'D %s %s' % (user, word)
    if c.send1(message):
        c.recv1()
def history(user,c):
    message = 'H %s %s'%(user,'a')
    if c.send1(message):
        c.recv1()
        return
    print('没有记录')
def jiami(password):
    salt = '%$@%&%*^$#%$@%&%*^$#%$@%&%*^$#%$@%&%*^$#%$@%&%*^$#%$@%&%*^$#'
    list1 = []
    for i in range(len(salt)):
        list1.append(salt[i])
        try:
            list1.append(password[i])
        except:
            print(''.join(list1))
            password1 = ''.join(list1)
            hash = hashlib.md5()
            hash.update(password1.encode())
            print(hash.hexdigest())
            return hash.hexdigest()

def main():
    s = socket.socket()
    s.connect(ADDR)
    c = Dict_client(s)
    while True:
        a=input('1注册,2登录,3退出')
        if a == '1':
            user = input('name:')
            password = input('password')
            password2 = jiami(password)
            message = 'IN %s %s' % (user, password2)
            if c.send1(message):
                print('注册成功')
                continue
            print('用户名已存在')
        elif a == '2':
            user = input('name:')
            password = input('password')
            password1 = jiami(password)
            message = 'ON %s %s' % (user, password1)
            if c.send1(message):
                print('登录成功')
                while True:
                    k = input('1查询单词，2查询历史，3返回，4，注销')
                    if k == '1':
                        dict(user,c)
                    elif k == '2':
                        history(user,c)
                    elif k == '3':
                        break
                    elif k == '4':
                        password = input('password')
                        password2 = jiami(password)
                        message = 'DE %s %s' % (user, password2)
                        if c.send1(message):
                            print('注销成功')
                        else:
                            print('注销失败，请重试')
            else:
                print('用户名/密码错误')
        elif a == '3':
            message = 'Q %s %s'%(1,2)
            c.send1(message)
            c.c.close()

if __name__ == '__main__':
    main()





