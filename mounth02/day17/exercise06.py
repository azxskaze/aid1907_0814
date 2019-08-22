'''生成器
    生成一次 计算一次 返回一次
    延迟操作/惰性操作
'''
list01=[1,2,3,4,5,6]
'''传统方式很费内存'''
def even(args):
    list01=[]
    for i in args:
        if int(i)%2==0:
            list01.append(i)
even(list01)

'''生成器方式节省内存'''
def even1(list):
    for i in list:
        if i%2==0:
            yield i
'''只有在调用数据的时候才会开始生成数据
    光调用函数提并不会生成
    在调用之前不需要占用实体内存
    even1（list01）
    只是一个生成器
    而list(even1(list01))
    才是存储有数据的容器'''
print(list(even1(list01)))