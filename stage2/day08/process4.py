'''进程函数传参
'''
from multiprocessing import Process
import time

# 带参数的函数
def worker():
    for i in range(3):
        time.sleep(1)
        print('working')

p = Process(target=worker,name='ly')
p.daemon = True
'''daemon 父进程一旦结束，子进程立即解除
    定义了daemon就不用再写join了，一般不和join一起使用'''
p.start()
time.sleep(2)
print(p.name)
print(p.pid)
print(p.is_alive())
p.join()
print(p.name)
print(p.pid)
print(p.is_alive())