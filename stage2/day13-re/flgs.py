import re
s = '''Hello
北京'''
p1 = '\w+'
re1 = re.compile(p1,flags=re.A)#只能匹配ascii

# re2 = re.compile('[a-z]+',flags=re.I)#忽略大小写

# re3 = re.compile(r'.+',flags=re.S)#让‘.’可以匹配换行

re4 = re.compile(r'Hello$',flags=re.M)#可以匹配每行的开头结尾位置

l = re4.findall(s)

p2 = '''\w+ #匹配Hello
\s #匹配换行
\w+ %匹配 北京'''

re5 = re.compile(p2,flags=re.X)#添加注释（注释可以写在正则表达式里面）
l1 = re5.findall(s)

print(l1)