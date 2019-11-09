'''map函数为map(fun,key),对输入的值进行循环执行fun
    reduce函数为reduce(fun(a,b),对输入的列表取循环取出一位和之前的结果执行fun)'''
from functools import reduce

# 可以对列表中的所有元素进行筛查转换，最后结果需要转换成list类型
l = map(lambda a:a+1,[1,2,3,4,5])
print(list(l))
# 相当于sum函数
print(reduce(lambda a,b:a+b,[1,2,3,4,5,6]))