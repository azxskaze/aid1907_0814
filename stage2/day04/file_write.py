'''
file_write
'''
# f=open('1.txt','w')
# f=open('1.txt','wb')
f=open('1.txt','a')
'''a追加的调用方法和w相同但是每次
不会清空，会追加上去'''


'''wb不能写入字节串,要写的话必须把字符串转化为字节串'''
# a='''ssssssssssssssgggddddddd
# 55656
# 8585
# 85
# 8'''
# f.write(a.encode())
# f.write('''hello world\n'''.encode())

'''
如果不想让两次写入连在一起要手动添加\n
'''
l=['a','b\n']

f.writelines(l)

# f.writelines() 不常用,将列表写成一行

f.close()
