'''sem 信号演示
注意：信号量相当于资源，多个进程对数量进行控制
'''

from multiprocessing import Semaphore,Process
import time,os

# 创建信号量(最多允许三个任务)
semm = Semaphore(3)
# 任务函数
def handle():

    semm.acquire()#执行任务必须消耗一个信号量

    print('任务开始：',os.getpid())
    time.sleep(2)
    print('任务结束：',os.getpid())

    semm.release()#任务执行结束释放一个信号量

for i in range(10):
    p = Process(target = handle)
    p.start()



