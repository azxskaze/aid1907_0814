'''wait  处理僵尸进程
通过wait阻塞函数来监听子进程结束状态，当子进程结束后，
wait语句之后才会执行'''
import  os
import time

pid = os.fork()
if pid < 0:
    print('Error')
elif pid == 0:
    time.sleep(0)
    print('Child process',os.getpid())
    os._exit(3)#进程退出
else:
    pid,status = os.wait()#阻塞等待回收子进程
    print('parent process',pid)
    print('status',status)
    while True:#让父进程不退出
        pass


