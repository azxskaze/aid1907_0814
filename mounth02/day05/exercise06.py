'''三引号作用：做见即所得，三引号里面不论怎么写，打印出来的格式
文字都和输入的一致'''
print('''sa
sa
sa
s                          sa
           s
                                       s''')
print(r'ss/n/t//')
'''r+字符串可以屏蔽字符串中的左右转义符号输出纯文本'''
s='张三'
q=20
t=55.55
print('%s同学年龄是:%d体重是：%.2f'%(s,q,t))
'''占位符'''
print()
str01=input('请输入字符串：')
for chr01 in str01:
    print(ord(chr01))

while True:
    chr_num=input('请输入编码值：')
    if chr_num=='':
        break
    else:
        print(chr(int((chr_num))))