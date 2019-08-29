'''缓冲区'''
# f = open('3.txt','a',1)
# 行缓冲，每执行完一行
# 会刷新缓冲写到磁盘
f = open('3.txt','a')#无规定缓冲，
# 当程序执行完或者关闭文件才会刷新缓冲区
while True:
    data = input('>>')
    if not data:
        break
    f.write(data+'\n')
    f.flush()
    '''f.flush 主动刷新缓冲区'''