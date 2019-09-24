'''fork.py  fork 进程展示'''
import  os
pid = os.fork()

if pid < 0:
    print('create process daied')
elif pid == 0:

    print('the new process')
else:
    print(pid,'the old process')
print('fork test over')
