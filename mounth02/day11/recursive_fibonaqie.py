'''python3
中的最大递归深度为998
超过的话会报错
如果需要增大
import sys
sys.setrecursionlimit(i+2)
如果超过998，则最大递归深度至少+2
'''
'''斐波那契数列递归法'''
def fun(a,b,c,list):
    a,b=b,a+b
    c+=1
    if c>997:
        return 0
    list.append(a)
    return fun(a,b,c,list)
list1=[0]
fun(0,1,0,list1)
print(list1)
