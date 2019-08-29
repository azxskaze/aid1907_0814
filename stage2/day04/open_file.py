# import
'''python字节串bytes
    表达二进制的一种方法'''
s=b'sas'
'''（ascii）字符串前面加上 b 
就表示python里面的字节串'''
print(type(s))
'''非ascii字符可以调用encode（）方法转换为字节串'''
s1='你好'.encode()
print(type(s1))
s2=s1.decode()
'''bytes类型通过decode转化为字符串
（不一定是所有的字节串都能转化为字符串《
编码库中可能不存在某些编码或者编码表示的本来就不是字符串》）'''
print(type(s2))
