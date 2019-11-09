'''sorted可以按照key中的条件进行排序，
lamba是匿名函数'''
dic = {'a':5,'b':6,'c':1}
di = sorted(dic.items(),key=lambda  x:x[1])
dj = sorted(dic)
print(di,dj)

'''输出字符串的内键方法'''
print(dir('a'))
