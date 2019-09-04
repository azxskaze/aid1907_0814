str1='123123321321'
# 连续删除头部所有匹配字符，连续删除尾部反向匹配字符
print(str1.strip('123'))
# format多功能格式化字符串，按照指定格式重构字符串
# 可以是位置传参或者关键字传参，字典列表对象都可以进行操作


print("a1:{a},b1:{b}".format(a='aaaaa',b='bbbbbbbb'))
a='{0}{1}{0}{1}'.format('no','so')
print(a)
dict1={'name':'zs','age':'17'}
s1='姓名：{name},年龄：{age}'.format(**dict1)
print(s1)
l=['ls',18]
s2='姓名:{0[0]},年龄:{0[1]}'.format(l)
print(s2)
class S:
    def __init__(self,val):
        self.val = val
s=S('ww')
s3='name:{0.val}'.format(s)
print(s3)