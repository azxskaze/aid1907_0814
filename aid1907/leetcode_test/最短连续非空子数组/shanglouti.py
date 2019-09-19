'''上楼梯问题动态规划
递归解决
'''
k = 0

def fun(n):
    global k
    # try:
    #     nonlocal str1
    # except SyntaxError:
    #     str1 = ''
    str1 = ''
    if n==1:
        k += 1
        return '1'
    if n == 0:
        k += 1
        print(str1)
        return ''
    yield '1',fun(n-1)
    yield '2',fun(n-2)

def fun2(x):
    for i,g in x:
        print(i)
        fun(g)

fun2(fun(2))
# for i,g in fun(10):
#     for i in g:
#         print(i)
print(k)
11111
1121
1112
1211
122
2111
212
221

