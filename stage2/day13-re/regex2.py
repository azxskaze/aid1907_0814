'''match 对象属性方法演示'''
import re
pattern = r'(ab)cd(?P<pig>ef)'
regex = re.compile(pattern)
obj = regex.search('abcdefjkhikuj')
print(obj.group())

# print(obj.pos)#目标字符串开始位置
# print(obj.endpos)#目标字符串结束位置
# print(obj.re)#正则
# print(obj.string)#目标字符串(整个字符串)
# print(obj.lastgroup)#获取最后一组的组名
# print(obj.lastindex)#获取最后一组的组号

# 属性方法
print(obj.span())#匹配内容在目标字符串的位置
print(obj.start())#匹配内容在目标字符串的开始位置
print(obj.end())#匹配内容在目标字符串的结束位置

print(obj.groupdict())#捕获组的组名与其对应的内容的字典
print(obj.groups())#子组对应内容（所有）
print(obj.group(1))#获取第1组内容（传参：组号/组名）