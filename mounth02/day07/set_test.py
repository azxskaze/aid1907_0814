''''''
'''集合相当于只有键没有值的字典'''
'''集合的基础操作'''
list02=['1','2']
set01=(list02)
print(set01)
set02='abc'
print(set02)
set03=['abc']
print(set03)
set04=set('abca')
print(set04)
set04.update(('p','m'))
set04.update('str')

'''可以拆开里面的元素,
例如输入字符串会把单个字符一一添加'''
set04.add(('q','o'))
set04.add('chr')

'''add将一个不可变对象（int str tuple）放到集合
不能放入列表因为不能拆
例如输入字符串会把整个字符串当成一个对象添加
'''
print(set04)
'''只能用for循环来获取元素，没有其他容器的方法'''
