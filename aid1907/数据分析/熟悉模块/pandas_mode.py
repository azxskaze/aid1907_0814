'''了解熟悉`pandas模块
可以去官网学习查看
'''
import pandas as pd

'''其中scv文件中的每一项数据称为Series
pandas中包含一个Series模块，暂不了解
'''
# 创建标签矩阵
# 方法一 pd.Series(list,index)
# s = pd.Series([1,2,3,4,5],index=['a','b','c','f','e'])
# 方法二
# pd.Series(dict)
# s = pd.Series({'a':3,'b':4,'c':5,'f':6,'e':8})
# print(s)

# 读取数据
# read_csv不仅可以读取csv文件还可以通过设置参数还可以指定其他文件
# eg：read_csv(filepath,sep='\t')
df = pd.read_csv('/home/tarena/PycharmProjects/aid1907/aid1907/数据分析/HR.csv')
# 显示一下读取数据
print(df)
print(type(df))
# 查看单项'satisfaction_level'类型
print(type(df['satisfaction_level']))
# 求均值
print(df.mean())
# 求出的平均值为Series类型的数据
print(type(df.mean()))
# 直接求均值得到的结果就是值(float类型)
print(df['satisfaction_level'].mean())
print(type(df['satisfaction_level'].mean()))
# 中位数
print('*')
print(df.median())
print(type(df.median()))
print(df['satisfaction_level'].median())
# 同样是Series类型的数据
print(type(df['satisfaction_level'].median()))

# 分位数（四等分，类似）
print(df.quantile(q=0.25))
print(df['satisfaction_level'].quantile(q=0.25))

# 众数(有可能不唯一)
print(df.mode())
print(df["department"].mode())
print(type(df["department"].mode()))

# 离中趋势
# std() 标准差
print(df.std())
print(df['satisfaction_level'].std())
# var()方差
print(df.var())
print(df['satisfaction_level'].var())
# sun()求和
print(df.sum())
# 离散数据求和相当于字符串相加
print(df['satisfaction_level'].sum())

# 偏态系数
# skew()函数
print(df.skew())
print(df['satisfaction_level'].skew())
# 偏态系数为负说明大部分数据都大于平均值，少量数据远小于平均值 可衡量数值分布情况
# 偏态系数为正说明大部分数据都小于平均值，少量数据远大于平均值

# 峰态系数
print(df.kurt())
print(df['satisfaction_level'].skew())

# pandas不能直接生成分布函数，需要借助 scipy.stats 这个统计包来生成
import scipy.stats as ss
# ss.norm是一个正态分布对象
print(ss.norm)
# ss.norm.stats()查看属性
# m-均值 v-方差 s-偏态系数 k-峰态系数
print(ss.norm.stats(moments='mvsk'))

# pdf分布函数指定横坐标，返回纵坐标的值
# 标准正态分布
print(ss.norm.pdf(0.0))

# ppf表示从负无穷到输入值（积分）的累计值
print(ss.norm.ppf(0.9))
# cdf表示从负无穷开始积分一直到输入值的累计概率
print(ss.norm.cdf(2))
# 整两倍的标准差减去负两倍的标准差的概率（95.4499736）这是一个固定值
print(ss.norm.cdf(2)-ss.norm.cdf(-2))

# 产生正态分布的数字 size指定数量
print(ss.norm.rvs(size=10))

# 其他三种分布的操作同正态分布
# 卡方分布
print(ss.chi2)
# t分布
print(ss.t)
# f分布
print(ss.f)


# 抽样 n指定样本个数
print(df.sample(n=10))
# frac指定样本比例
print(df.sample(frac=0.001))

# Series也可以抽样
