import re
def fun():
    f = open('exc.txt','r')
    port = input('请输入')

    str1=''
    s = f.readlines()
    n=0
    for i in s:
        # print(i.split(' '))
        if i.split(' ')[0]==port:
            str1+=i
            n=1
        elif i =='\n':
            if n == 1:

                break
        if n == 1:
            str1+=i
    else:
        return '不存在'
    re1 = re.search(r'Internet address is (\d+?\.\d+?\.\d+?\.\d+?\/\d+?)',str1)
    if re1.group(1) is None:
        print('没有ip')
    return re1.group(1)
print(fun())





