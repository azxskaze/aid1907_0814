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

