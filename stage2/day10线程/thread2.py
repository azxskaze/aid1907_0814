from threading import Thread
import time

# 含有参数的线程函数
def fun(sec,name):
    print('%s线程开始执行'%name)
    time.sleep(sec)
    print('%s线程执行完毕'%name)

# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun,args=(2,),kwargs={'name':'%d线程'%i})
    jobs.append(t)
    t.start()
for i in jobs:
    i.join()