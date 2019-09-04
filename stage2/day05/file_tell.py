f = open('1.txt','wb+')
'''文件名.tell()
    查看文件偏移量'''
print(f.tell())
f.write(b'aaaaaaaa')
print(f.tell())

print(f.read().decode())
print('*')
f.seek(55)
# f.write(b'aaaaaaaa')

print(f.read().decode())
print(f.tell())
f.close()

f = open('1.txt','rb+')
print(f.read().decode())

'''seek(offset[,whence])
一般用二进制打开，文本打开第二额参数只能是0
偏移量移动,向前越界会报错
想后越界在写操作时会填充[]'''
