'''
value 数据单一 多个进程操作
注意：value共享内存只能有一个值
'''
from multiprocessing import Process,Value
import time
import random

# 创建共享内存
money = Value('i',5000)

# 操作内存
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1,1000)
def gril():
    for i in range(30):
        time.sleep(0.15)
        money.value -= random.randint(100,800)
p1 = Process(target=man)
p2 = Process(target=gril())
p1.start()
p2.start()
p1.join()
p2.join()

print('一个月余额：',money.value)