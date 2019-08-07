
dict01={k:k**2 for k in range(10) if k>5}
print(dict01)

'''dict.update(dict2)
如果dict2中的键在dict不存在，则追加进去
如果存在，就改写'''

dict05={1:5,9:9}
'''1:5-->追加
   9:9-->改写'''
dict01.update(dict05)
print(dict01)

'''dict.get(k)
获取键k的值
如果k不存在返回None'''
print(dict01.get(7))

'''dict.setdefault
获取键k的值
如果k不存在新建一个k
值设为None
'''
print(dict01.setdefault(11))

list01=['张三丰','翠山','无忌']
dict02={k:len(k) for  k in list01}

list03=['无忌','张敏','芷若']
list04=[101,102,103]

dict04={list03[i]:list04[i] for i in range(len(list03))}

print(dict02,dict04)