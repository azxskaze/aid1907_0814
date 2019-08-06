
'''字符串为不可变类型，字
符串的切片地址不变相当于整形存储方式

列表为可容器，切片后相当于浅拷贝'''

a='ssssaaa'
b=a[:]
c='ss'
d='sa'
print(a is b)
print(c in a,d in a)
'''in 可以判断单个字符和字符串'''
list01=['a','b','c']
list02=list01[:]
print(list02)
print(list01 is list02)
list03=['a','b']
list04='b'
f='a'
print(list03 in list01,list04 in list01,f in list01)
'''只能判断一个元素或者只包含一个元素的列表，
不能判断包含多个元素的列表'''
