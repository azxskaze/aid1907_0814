# 面试题：能够参与for循环的对象
# 必须具备什么样的条件
'''对象必须有__iter__()方法'''
list1=[10,11,12,13,14,15]
# for item in  list1:
#     print(item)
# for循环的原理
#通过__iter__()方法能够获取迭代器对象iterator
iterator = list1.__iter__()
iterator1 = list1.__iter__()
iterator2 = list1.__iter__()
item=iterator.__next__()
while True:
    # 如果迭代器中美域可以继续__next__()
    # 会抛出停止迭代异常
    try:
        item=iterator.__next__()
        print(item)
    except StopIteration:
        print('meile')
        break
for item in iterator1:
    print(item)
    '''一个迭代器只能循环一次，
    循环结束的时候迭代器里面就没有东西了'''
for item in iterator:
    print(item)