'''child 二级子进程
    让一级子进程做他应该做的事，正常关闭就行
    父进程用wait()语句等待一级子进程结束，
    但是wait()之后的事情交给二级子进程
    用一个二级子进程来做本来应该在wait()语句之后的事情
    实现并发的效果
'''
import  os
import time
pid = os.fork()
if pid < 0:
    print('Error')
elif pid == 0:
    pid1 = os.fork()
    if pid1 < 0:
        print('失败')
    if pid1 == 0:
        print('二级子进程来做本来应该是父进程的事情：')
        print('22222',os.getpid())
        print('parent process', os.getpid())
        for i in range(50):
            print(i)
    else:

        print('Child process',os.getpid())
        print('子进程应该做的事')

        print('让二级子进程变成孤儿')
        os._exit(3)#进程退出
else:
    time.sleep(2)
    pid,status = os.wait()
    print('交给二级子进程')
    s = os.getpid()
    print('give next')






