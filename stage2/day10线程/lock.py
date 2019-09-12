'''
thread_lock
线程锁演示
'''
from threading import Thread,Lock

lock = Lock()
a = b = 0
def value():
    while True:
        lock.acquire()
        if a != b:
            print(a,b)
        lock.release()
t = Thread(target=value)
t.start()
while True:
    with lock:
        a += 1
        b += 1
t.join()
