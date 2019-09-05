'''复制文件'''
from multiprocessing import Pool
import os
list_file=os.listdir('/home/tarena/学习笔记/第二阶段/IO网络编程 (1)/IO网络编程/img')
old_path = '/home/tarena/学习笔记/第二阶段/IO网络编程 (1)/IO网络编程/img'
new_path = '/home/tarena/桌面/img'



def worker(old,new):
    f = open(old, 'rb')
    # size1 = os.path.getsize(old)
    f2 = open(new, 'wb')
    f2.write(f.read())
    # q.put(os.path.getsize(old))

    f.close()
    f2.close()
pool1 = Pool()
for i in list_file:
    old = old_path+'/'+i
    new = new_path+'/'+i
    pool1.apply_async(worker,args=(old,new))
pool1.close()
pool1.join()
