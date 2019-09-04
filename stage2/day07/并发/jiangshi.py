'''wait  处理僵尸进程
当子进程退出时，父进程没有及时进行处理（sleep（1），
子进程就会变成僵尸进程，在 pa -aux能看到一个Z+）
'''
import  os
import time
pid = os.fork()
if pid < 0:
    print('Error')
elif pid == 0:

    print('Child process',os.getpid())
    os._exit(3)#进程退出
else:
    time.sleep(1)
    print('parent process',os.getpid())
    while True:
        pass





