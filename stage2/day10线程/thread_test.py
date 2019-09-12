"""
测试用例
"""
from threading import Thread
from multiprocessing import Process
import time


def ttime(fun):
    def pack(*args,**kwargs):
        a = time.time()
        fun(*args,**kwargs)
        print(time.time()-a)
    return pack

# 计算

def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

# io
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(1700000):
        f.write("Hello world\n")
    f.close()

def read():
    f = open('text')
    lines = f.readlines()
    f.close()
@ttime
def cs(count1,args=()):
    for i in range(10):
        count1(*args)
# cs(count,(1,1))
# 7.372812509536743
# cs(io)
# 5.031578302383423


# 进程
@ttime
def cs1(count1,args=()):
    list1 = []
    for i in range(10):
        p = Process(target=count1,args=args)
        list1.append(p)
        p.start()
    for i in list1:
        i.join()
# cs1(count,(1,1))
# 3.570000410079956
# cs1(io)
# 1.383617639541626
@ttime
def cs2(count1,args=()):
    list1 = []
    for i in range(10):
        p = Thread(target=count1,args=args)
        list1.append(p)
        p.start()
    for i in list1:
        i.join()
# cs2(count,(1,1))
# 9.220926761627197(比单线程还惨，five)
# cs2(io)
# 4.039166450500488(多进程只要1.4秒)five