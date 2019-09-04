'''get_pid 获取进程号
getpid()获取当前进程号
getppid()获取父进程进程号'''


import  os

pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    print('Child process',os.getpid(),' ',os.getppid())
else:
    print('parent process',pid)


