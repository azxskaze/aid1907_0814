'''os.exit()参数必须给，参数为整数，可以随便给，
也可以约定（0正常退出，其他自定义）

sys.exit()默认值为0，还可以传字符串'''


import  os,sys

# os._exit(0)
sys.exit('进程退出')

print('parent process')


