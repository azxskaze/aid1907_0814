import re
'''正则表达式'''
# regex='[123]\\d{5}'
# telnumber=str(145684)
# print(telnumber.matches(regex))
pattern = re.compile('foo')
res1 = re.search(pattern,'foo')
print(res1.group())

res2 = re.findall(pattern,'foobbfoo')
print(res2)
pattern2 = re.compile(r'(\d)aa')
res3 = re.search(pattern2,'bb32aa')
print(res3.group())