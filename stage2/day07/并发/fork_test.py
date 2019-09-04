'''fork.py  fork 进城展示'''
import  os
from  time import sleep
pid = os.fork()
if pid < 0:
    sleep(4)
    print('create process daied')
elif pid == 0:
    sleep(4)
    print('the new process')
else:
    sleep(4)
    print(pid,'the old process')
print('fork test over')
