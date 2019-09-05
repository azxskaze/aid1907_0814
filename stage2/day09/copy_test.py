'''有大量事件，频繁创建进程会消耗系统资源
进程池实例（爬虫可能会用）'''
'''
定义方法需要在Pool之前
'''
from multiprocessing import Pool,Queue
import os
# new_path = '/home/tarena/PycharmProjects/aid1907/stage2/day09/chat'
# old_path = '/home/tarena/PycharmProjects/aid1907/stage2/day08/群聊聊天室/chat'
# list_file=os.listdir('/home/tarena/PycharmProjects/aid1907/stage2/day08/群聊聊天室/chat')

list_file=os.listdir('/home/tarena/学习笔记/第二阶段/IO网络编程 (1)/IO网络编程/img')
old_path = '/home/tarena/学习笔记/第二阶段/IO网络编程 (1)/IO网络编程/img'
new_path = '/home/tarena/桌面/img'
q = Queue(5)
# 进程池执行
def worker(old,new):
    f = open(old, 'rb')
    f2 = open(new, 'wb')
    f2.write(f.read())
    q.put(os.path.getsize(old))
    f.close()
    f2.close()
size = 0
for i in list_file:
    # print(os.path.getsize())
    size += os.path.getsize(old_path+'/'+i)
def ttime():
    size1 = 0
    print('本次共移动%fM:'%(size/1024/1024))
    while size1<size:
        size1 += q.get()
        print('进度为百分之%.1f'%((size1/size)*100),sep='')
pool1 = Pool()
# 添加事件
pool1.apply_async(ttime)
for i in list_file:
    old = old_path+'/'+i
    new = new_path+'/'+i
    pool1.apply_async(worker,args=(old,new))
# 关闭进程池（不能再添加新事件了）
pool1.close()
# 回收进程池
pool1.join()
