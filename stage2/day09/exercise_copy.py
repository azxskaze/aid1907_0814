import os
from multiprocessing import Pool
list_file=os.listdir('/home/tarena/PycharmProjects/aid1907/stage2/day08/群聊聊天室/chat')
old_path = '/home/tarena/PycharmProjects/aid1907/stage2/day08/群聊聊天室/chat'
list_old_path = []
size = 0
list_open = []
'''打开文件f'''
list_new_file = []
'''新文件path'''
list_write = []
'''写入文件f'''
new_path = '/home/tarena/PycharmProjects/aid1907/stage2/day09/chat'
for i in list_file:
    # size += os.path.getsize(i)
    list_old_path.append(old_path+'/'+i)
for i in list_old_path:
    list_open.append(open(i, 'r'))

for i in list_file:
    print(new_path + '/'+i)
    list_new_file.append(new_path+'/'+ i)

for i in list_new_file:
    print(i)
    list_write.append(open(i,'w'))

for i in range(len(list_open)):
    list_write[i].write(list_open[i].read())
    print('ok')
    list_write[i].close()
    list_open[i].close()
