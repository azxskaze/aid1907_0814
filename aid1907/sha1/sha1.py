'''python位运算  逻辑与 &   亦或\  非~
    int(str,2)      将字符串从二进制转化为10进制'''
a=ord(b'a')
b=bin(a)+bin(10)
print(int('101',2))
print(int(b.replace('0b',''),2))
print()
print(len(bin(a)))
print(a)
c=ord(b'c')
print(a|c)
print((a&c))