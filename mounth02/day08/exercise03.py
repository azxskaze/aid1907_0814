count=0
def myprint():
    global count
    '''
    将count声明为全局变量
    '''
    count+=1
    return count

print(myprint())
print(myprint())
print(myprint())
print(myprint())