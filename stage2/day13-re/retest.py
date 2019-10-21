import re
s='sasa@dsd54.com,sauifd@8tg.cn'
pattern = r'\S+@\S+\.(com|cn)'
print(re.findall(pattern,s))
# regex = re.compile(pattern)
# l = regex.search(s)
l = re.finditer(pattern,s)


for i in l:
    print(i.group())
# l = re.match(pattern,s)
# print(l)