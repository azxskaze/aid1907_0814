a=['a','b','c',]
b=a[:]
a.append('d')
print(a,b)

'''
切片
定义上是浅拷贝（地址没变）
并不是完全浅拷贝
既有浅拷贝的属性也能做深拷贝的行为
数据没有多复制出来一份，
但是对新数据的操作不会改变原数据
'''