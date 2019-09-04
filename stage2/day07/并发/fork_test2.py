'''fork.py  fork 进城展示'''
import  os
from  time import sleep
print('==================')
pid = os.fork()
if pid < 0:
    print('Error')
elif pid == 0:
    print('Child process')
else:
    print('parent process')
print('fork test over')
