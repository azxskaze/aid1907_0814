'''装饰器'''

def fun01(n):
    a=n
    return a,1,2


@fun01
def fun(n):
    return n

a=fun(5)
print(a)