''''''
# 打开文件
try:
    '''文本文件既可以使用文本方式打开，也能使用二进制方式打开
        
        二进制文件如果使用文本方式打开，读写时会报错'''

    # file_object = open('1.txt','r')
# 读取文件
# r只读的方式，文件必须存在，不存在会报错
#     file_object = open('test_file.py', 'w')
#w只写的方式，文件不存在就会新创建文件，存在就会清空文件
      # file_object = open('est_file.py', 'a')
#a读写的方式，文件不存在就会新创建文件，存在就会追加
except Exception as e:
    print(e)
# file_object = open('1.txt','rb')
# rb以二进制格式打开
file_object = open('2.txt','r')
# readline([size])可以传参数，每次打开的个数
# while True:
#     a=file_object.readline(6)
#     if not a:
#         break
#     print(a,end='')
# readlines()将内容读取到一个列表，每一行就是列表的一个元素
#     传的参数到了第几行，就把这些行都添加到列表中
a=file_object.readlines()
for i in a:
    print(i)

# 文件对象可迭代,每次迭代一行
# for line in file_object:
#     print(line)


file_object.close()
# close()关闭文件方法节省内存


# b='llllllll'
