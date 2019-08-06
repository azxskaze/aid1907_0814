str01=input('plz')
print('第一个字符是%s\n倒数第二个字符是%s\n前两个字符是%s\n倒序打印：%s\n奇数%s\n%s'%
      (str01[0],
       str01[len(str01)-2],
      str01[:2],
       str01[::-1],
       str01[::2],
       str01[int(len(str01)/2)] if len(str01)%2 else ''))







# list02=str01[int(len(str01)/2)] if len(str01)%2!=0 else None
# print('%s'%str01[int(len(str01)/2)] if len(str01)%2!=0 else None)