'''
父进程先于子进程退出

孤儿进程不会变成僵尸
'''


import  os,sys
import time
pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    time.sleep(1)
    print('Child process',os.getpid(),' ',os.getppid())
else:

    print('parent process',pid)

sys.exit()
