'''
multiprocessing 模块城建进程

1. 编写进程执行函数
2. 创建进程对象
3. 启动进程
4. 回收进程
'''
import multiprocessing as mp
import time

a = 1

# 进程函数
def fun():
    global a
    print(a)
    a = 10000
    '''只能修改子进程自己的变量
        不影响父进程
        '''
    print('开始一个进程')
    time.sleep(3)
    print('进程结束')

# 创建进程对象
# target = 函数名，不加括号
p = mp.Process(target = fun)
p.start()#启动进程
time.sleep(2)
print('父进程')
print(a)
p.join(0.5)#回收进程
print('===========')
'''
p = os.fork()
if pid == 0:
    fun()
else:
    os.wait()
'''