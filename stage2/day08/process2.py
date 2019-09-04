'''同时创建多个子进程'''
from multiprocessing import Process
import time
import os
def th1():
    time.sleep(3)
    print('恰饭')
    print(os.getpid(),'--',os.getppid())
def th2():
    time.sleep(5)
    print('睡觉')
    print(os.getpid(),'--',os.getppid())
def th3():
    time.sleep(4)
    print('打豆豆')
    print(os.getpid(),'--',os.getppid())

things = [th1,th2,th3]
'''先用一个列表提前存储一下对象，
等到都启动后再回收'''
jobs = []
'''同时创建多个进程'''
for th in things:
    p = Process(target = th)
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
