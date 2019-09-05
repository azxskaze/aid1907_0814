'''复制文件'''
import os,time
from multiprocessing import Pool,Queue
# list_file=os.listdir('/home/tarena/学习笔记/第二阶段/IO网络编程 (1)/IO网络编程/img')
# old_path = '/home/tarena/学习笔记/第二阶段/IO网络编程 (1)/IO网络编程/img'
# new_path = '/home/tarena/桌面/img'
new_path = '/home/tarena/PycharmProjects/aid1907/stage2/day09/chat'
old_path = '/home/tarena/PycharmProjects/aid1907/stage2/day08/群聊聊天室/chat'
list_file=os.listdir('/home/tarena/PycharmProjects/aid1907/stage2/day08/群聊聊天室/chat')

p1 = Pool()
def copy(old,new):
    f = open(old,'rb')
    f2 = open(new,'wb')
    f2.write(f.read())
    print('1111111111111')
    f.close()
    f2.close()
# def total_time():
#     print(11111)
#     # size = 0
#     # for i in list_file:
#     #     size += os.path.getsize(old_path + '/' + i)
#     # size1 = 0
#     # print(size1)
#     # while size1<size:
#     #     size1+=q.get()
#     #     print(size1)
#     #     print('进度为')

# p1.apply_async(total_time)
for i in list_file:
    old = old_path+'/'+i
    new = new_path+'/'+i
    p1.apply_async(copy,args=(old,new))
p1.close()
p1.join()