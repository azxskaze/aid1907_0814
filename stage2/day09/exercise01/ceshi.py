import os,time
from multiprocessing import Pool,Value
list_file=os.listdir('/home/tarena/学习笔记/第二阶段/IO网络编程 (1)/IO网络编程/img')
old_path = '/home/tarena/学习笔记/第二阶段/IO网络编程 (1)/IO网络编程/img'
new_path = '/home/tarena/桌面/img'

for i in list_file:

    print(os.path.getsize(old_path+'/'+i))