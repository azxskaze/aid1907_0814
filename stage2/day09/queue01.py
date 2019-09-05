'''queue01 消息队列
注意： 通过一个对象操作队列，满足先进先出原则
'''
from multiprocessing import Queue,Process
import time
import random

# 创建消息队列
q = Queue(5)

# 请求进程
def request():
    for i in range(10):
        time.sleep(0.5)
        t = (random.randint(1,100),random.randint(1,100))
        q.put(t)
        print('===========')

# 数据处理进程
def handle():
    sum1=0
    while True:
        sum1+=sum(q.get())
        print(sum1)
        time.sleep(1)

if __name__ == '__main__':
    p1 = Process(target=request)
    p2 = Process(target=handle)
    p1.start()
    p2.start()
    p1.join()
    p2.join()