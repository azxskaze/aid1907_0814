from day02.link_strack import StrackLink
s1=StrackLink()
s2=StrackLink()
def push(val):
    s1.push(val)
def pop():
    while s1.is_empty() is not True:
        s2.push(s1.pop())
    a=s2.pop()
    while s2.is_empty() is not True:
        s1.push(s2.pop())
    return a
push(1)
push(2)
print(pop())
print(pop())
push(3)
push(2)
push(5)
print(pop())
push(4)
push(8)
push(6)
push(8)
push(9)
push(7)
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())
print(pop())






