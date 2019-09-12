'''
thread  与Process非常相似
步骤： 1.封装线程函数
2.创建线程对象
3.启动线程
4.回收线程
主线程和分支线程属于同一线程进程号相同
'''
import threading
import time
import os
# 线程函数
a = 1
def music():
    '''子线程对全局变量的操作会
    影响到主线程（同一代码空间）'''
    global a
    print(a)
    a = 10000
    for i in range(3):
        time.sleep(2)
        print(os.getpid(),'分线程事件',a)

# 创建线程对象(分支线程)
t = threading.Thread(target = music)
# 启动线程
t.start()

for i in range(4):
    time.sleep(2)
    print(os.getpid(),'主线程事件',a)


# 回收线程(不手动回收也没事)
t.join()