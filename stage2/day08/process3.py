'''进程函数传参
'''
from multiprocessing import Process
import time

# 带参数的函数
def worker(sec,name):
    for i in range(3):
        time.sleep(sec)
        print("I'm %s"%name)
        print('working')
# p = Process(target=worker,args = (2,'azxs'))
p = Process(target=worker,args= (2,),kwargs={'name':'ly'})
p.start()
p.join()