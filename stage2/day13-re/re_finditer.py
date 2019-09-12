'''
regex1
生成match对象的函数
'''
import re

s ='Alex:1997,Sunny:1996'
pattern = r'\d+'

# 返回迭代对象
re1 = re.finditer(pattern,s)
for i in re1:
    print(i.group()) #获取match对象匹配内容

# 完全匹配(相当于^pattern$)
obj =re.fullmatch(r'.+',s)
print(obj.group())

# 匹配开始(相当于^pattern)
obj = re.match(r'\w+',s)
print(obj.group())

# 匹配第一个符合内容（匹配一个后就不再匹配）
obj = re.search(r'\d+',s)
print(obj.group())
