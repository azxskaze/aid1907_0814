# dict01={'a':1, 'b':2, 'c':2, 'd':2, 'e':2}
# for key in dict01:
#     print(dict01[key])
# print(dict01)
# print(str(dict01))
# print(type(dict01))
dict01=dict(([1,23],(4,56)))
'''用列表和元祖创建字典键值对通过hash绑定
字典的读写速度快，但是无序，不能索引
字典结构占用内存空间较大'''
print(dict01)

dict01['o']=123
print(dict01)
print(123 in dict01)
print('o' in dict01)
d_o=dict01.pop('o')
print(dict01,d_o)
dict01[(1,2,3)]=123
'''字符串，字符，数字，元祖可以作为字典的键'''
print(dict01)
dict01[[4,5,6]]=456
'''列表不可以作为字典的键'''
