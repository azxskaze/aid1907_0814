import copy
'''切片不是深拷贝
切片后新的列表指向的还是原来对象，
（浅拷贝中的对象始终没变）
深拷贝会把对象复制一遍给新列表
见图'''
list01=['s','b','c',[1,2]]
# list02=list01
list02=list01[:]
list03=list01
list01[0]='8'
list01[3][0]=4
list03[2]=list01[2]
list03[2]=[]
print(list01,list02,list03)

# list02=copy.deepcopy(list01)
# list01[0]='c'
# print(list01,list02)