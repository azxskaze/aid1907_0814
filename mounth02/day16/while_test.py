'''通过递归实现遍历列表'''
list1=[0,1,2,3]
list_iter=list1.__iter__()
def fun():
    try:
        print(list_iter.__next__())
        fun()
    except StopIteration:
        pass
fun()
