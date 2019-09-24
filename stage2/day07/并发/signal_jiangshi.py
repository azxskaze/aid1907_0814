import os,signal
#信号处理僵尸
# signal.signal(signal.SIGCHLD,signal.SIG_IGN)
#在创建子进程之前写上就行
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
# 子进程退出时系统会发送消息给父进程，
# 父进程没有处理子进程将会变成孤儿进程
import time
pid = os.fork()
if pid < 0:
    print('Error')
elif pid == 0:
    time.sleep(0)
    print('Child process',os.getpid())
    print(pid)
    os._exit(3)#进程退出
else:
    time.sleep(1)
    print('parent process',pid)

