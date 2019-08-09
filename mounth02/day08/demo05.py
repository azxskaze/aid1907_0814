g01='悟空'
g02='八戒'
def fun01():
    num=100
    print(num)
    global g02
    g02='老猪'
    print(g02)
    global g03
    g03 = '老沙'
    # print(g03)
    # return locals()
fun01()
print(g03)
'''nonlocal
用法和global类似
后面跟嵌套变量'''
def fu():
    a=10
    def fu1():
        nonlocal a
        a+=1
        print(a)