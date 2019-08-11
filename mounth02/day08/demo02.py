# def fu(a,b,c):
#     print(a,b,c)
# t=(1,2,3)
# fu(*t)

''''''
'''函数参数传递
形参'''
def fun01(row,col,char='*'):
    """
打印矩形要求输入
打印的行数列数和填充字符
如果用户不传递填充字符 默认使用*
    :param row:
    :param col:
    :param char:
    """
    for i in range(row):
        for c in range(col):
            print(char,end=' ')
        print()
fun01(7,5,'-')

def fun02(a=0,b=0,c=0):
    """
完全默认形参
    :param a:
    :param b:
    :param c:
    """
    print(a)
    print(b)
    print(c)
fun02()
fun02(b=55)
'''参数不确定时使用*tuple
固定格式*args
可以无限匹配实参数据（无限数据0到任意多）'''
def fun03(p1,p2,*args):
    print(p1)
    print(p2)
    print(*args)
fun03(1,2,3,4,5,6,7,78)
fun03(1,2)
'''命名关键字实参
输入实参时*args后面的参数
必须要用默认形参或者命名关键字传参'''
def fun04(*args,p1,p2):
    print(*args)
    print(p1)
    print(p2)
fun04(1,2,3,4,5,p1=1,p2=5)

'''
eg
sep是每个值后面加的字符串
end是最后一个字符后面加的字符串
'''
def myprint(*args,sep=' ',end='\n',file=None):
    print(args,sep=sep,end=end)
myprint(1,2,3,4,sep='+')

'''
*星号以后的位置形参是命名关键字形参
传递实参只接受关键字实参
'''
def fun05(*,p1=0,p2):
    print(p1)
    print(p2)
fun05(p2=8)

'''
双星号字典传参
让关键字实参的数量无限
将关键字实参的变量名作为字典的键
然后值作为字典的值保存
'''
def fun06(**kwargs):
    print(kwargs)
fun06(a=10,b=20,c=30)

# def fun07(a=0,b,c):#位置形参要写在前面，这样写是不对的
#     print(a)
#     print(b)
#     print(c)
# fun07(b=20,c=60)#报错
'''只要出现关键字形参 后面的参数也要带关键字'''
def fun07(b,c,a=0):#位置形参要写在前面
    print(a)
    print(b)
    print(c)
fun07(10,20)

'''要求定义一个函数 函数中包含位置形参，星号元祖
形参默认形参，命名关键字形参和双星号字典形参'''
'''定义一个函数 接受任意的参数 并输出结果'''
def fun08(a,c=2,*args,b=4,d,**kwargs):
    print(a)
    print(c)
    print(b)
    print(args)
    print(d)

    print(kwargs)
fun08(10,9,30,1,2,3,d=5,b=99,f=6,g=7)

def fun09(*args,**kwargs):
    print(*args,kwargs)
fun09()

