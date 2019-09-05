'''
array 存放一组数据 共享内存
'''
from multiprocessing import Process,Array
import time
import random

# 创建共享内存,初始值为[1,2,3,4,5]
# shm = Array('i',[1,2,3,4,5])

# 创建共享内存,初始值为[0,0,0,0]
# shm = Array('i',4)

shm = Array('c',b'hello')

# 操作内存
def fun():
    # 迭代获取共享内存
    for i in shm:
        print(i)
    shm[0] = b'l'

p1 = Process(target = fun)
p1.start()
p1.join()

# for i in shm:
#     print(i)
print(shm.value)
'''
obj.value在array中只能用于打印字节串，不能打印列表
'''