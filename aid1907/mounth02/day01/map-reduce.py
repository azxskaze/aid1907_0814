from functools import reduce

def f(x):
    return x**2
a=map(f,[1,2,3,4,5])

for i in a:
    print(i)
print(a)


def fn(x,y):
    if x>y:
        return x
    return y
print(reduce(fn,[1,2,3,4,5,6,7,45,32,555]))

print(reduce(fn,map(f,[1,2,3,4,5,6,7,45,32,555])))




