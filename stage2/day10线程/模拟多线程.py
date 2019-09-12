'''多线程拷贝'''
from threading import Thread,Lock
import os,time

urls = ['/home/tarena/桌面/',
        '/home/tarena/下载/',
        '/home/tarena/音乐/',
        '/home/tarena/视频/',
        '/home/tarena/图片/',
        '/home/tarena/模板/',
        '/home/tarena/文档/'
        ]
list_have = []
# filename = input('要下载的文件：')
filename ='1'
for i in urls:
    # 判断是否在文件列表中
    # if filename in os.listdir(i):
    #     list_have.append(i+filename)
    # 或者判断是否在资源库路径中
    if os.path.exists(i+filename):
        list_have.append(i+filename)
print(list_have)
num = len(list_have)
size = 0
if list_have:
    size = os.path.getsize(list_have[0])
    block_size=size // num + 1
    print(size,block_size)
else:
    print('么得')
rout = input('请输入新路径：')
new = rout +'/'+ filename
f2 = open(new,'wb+')
lock = Lock()
def copy(i,size1,old):
    time.sleep(0.2)
    lock.acquire()
    f = open(old,'rb')
    f.seek(i*size1)
    print(f2.tell(),'*****',i)
    print(i*size1)
    f2.seek(i*size1)
    print(f2.tell(),'*',i)
    a = f.read(size1)
    f2.write(a)
    lock.release()
list_thread = []

for i in range(num):
    old= list_have[i]
    t = Thread(target = copy,args=(i,),kwargs={'size1':block_size,'old':old})
    list_thread.append(t)
    t.start()
for i in list_thread:
    i.join()
print('ok,da')
f2.close()

