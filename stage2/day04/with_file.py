'''python
with（只有固定的一些对象可以使用with语句）语句生成文件
with context_expression as obj:
    with-body'''
'''在with语句块中最文件进行操作后不需要关闭文件操作'''
with open('1.txt','r') as obj_file:
    print(obj_file.read())
'''with语句快结束，文件自动关闭'''
