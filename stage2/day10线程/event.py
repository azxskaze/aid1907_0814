'''
event 线程互斥方法演示
'''
from  threading import Thread,Event

s = None
e = Event()

def 杨子荣():
    print('杨子荣来了熬')
    global s
    s = '天王盖地虎'
    e.set()

t = Thread(target = 杨子荣 )
t.start()

print('来对口令')
e.wait()
if s == '天王盖地虎':
    print('宝塔镇河妖')
    print('对了嗷')
else:
    print('wdnmd')
t.join()