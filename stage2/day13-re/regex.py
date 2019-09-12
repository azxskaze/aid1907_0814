import re

s ='Alex:1997,Sunny:1996'
pattern = r'(\w+):(\d+)'

# l = re.findall(pattern,s)
# print(l)

# 正则对象调用
re1 = re.compile(pattern)

# l = re1.findall(s,0,10)#将s的0-9元素当成匹配目标

# l = re.split(r',',s) #将s按照‘，’进行切割

l = re.subn(r':','--',s,3)
# 将匹配到的内容替换微信内容，sub 和 subn不同是subn会返回替换的次数
print(l)
