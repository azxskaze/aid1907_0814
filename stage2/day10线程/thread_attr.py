'''线程属性演示'''
from threading import Thread
import time

def fun():
    time.sleep(3)
    print('进程属性设置')

t = Thread(target=fun,name='AID',daemon = True)

# 主线程退出，分支线程也立即退出，也不会和join一起使用
# t.setDaemon(True)

print('获取name:',t.getName())
t.setName('Tarena')
print('获取name:',t.getName())

print('is alive:',t.is_alive())
t.start()
print('is alive:',t.is_alive())

