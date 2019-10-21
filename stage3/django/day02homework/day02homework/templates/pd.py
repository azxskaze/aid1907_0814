from pandas import Series,DataFrame
import numpy as np
import time,random
import pandas as pd
# 带默认索引的列表
x1 = Series([1,2,3,4])
# 带指定索引的列表
x2 = Series(data=[1,2,3,4],index=['a','b','c','d'])
print(x1)
print(x2)
print(x2['a'])
data = {'Chinese': [66, 95, 93, 90,80],'English': [65, 85, 92, 88, 90],'Math': [30, 98, 96, 77, 90]}
df1= DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])
print(df1)
print(df2)