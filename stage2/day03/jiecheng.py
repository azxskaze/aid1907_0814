def jiecheng(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    return sum
print(jiecheng(3))
sum=1
def recursion(n):
    if n < 1:
        return 1
    else:
        return n * recursion(n-1)

print(recursion(3))
