'''
pipe.py 管道通信
注意：管道对象在父进程中创建，
子进程从父进程中获取
'''
from multiprocessing import Process,Pipe
'''Pool Pipe虽然是大写字母，但是是方法不是类'''
import time
# 创建管道
# 双向管道两个对象都能读写，单向管道只能左边接受右边发送fd2>>>>fd1
fd1,fd2 = Pipe()
def app1():
    print('app1,使用app2登录')
    print('向app2发请求')
    # 写管道
    time.sleep(3)
    fd1.send('app1需要：用户名，头像')
    data = fd1.recv()
    print(data,'登陆成功')
def app2():
    # 读管道
    data = fd2.recv()
    print('接受请求',data)
    time.sleep(3)
    print('发送')
    fd2.send({'name':'ly','image':'ly.jpg'})
list2 = []
list1 = [app1,app2]
for i in list1:
    p = Process(target=i)
    list2.append(p)
    p.start()
for i in list2:
    i.join()



