import random
import time
def big_number_add(num01,num02):
    global str_num01, str_num02, str_num03, num00, num0, max_len
    str_num01 = str(num01)
    str_num02 = str(num02)
    str_num03 = ''
    num00 = 0
    num0 = 0
    max_len = max(len(str_num01), len(str_num02))
    str_add()
    return add_to_no3()

def str_add():
    global i, str_num01, str_num02
    i = max_len - len(str_num01)
    if i > 0:
        for n in range(i):
            str_num01 = '0' + str_num01
    j = max_len - len(str_num02)
    if j > 0:
        for n in range(j):
            str_num02 = '0' + str_num02

def add_to_no3():
    global i, num0, num00, str_num03
    for i in range(max_len - 1, -1, -1):
        num0 = int(str_num01[i]) + int(str_num02[i]) + num0
        if 10 > num0:
            num00 = num0
            pass
        else:
            num00 = num0 % 10
        num0 //= 10
        str_num03 += str(num00)
    str_num03 = int(str_num03[::-1])
    return str_num03

# num01 = float(input('请输入大整数1：'))
# num02 = float(input('请输入大整数2：'))
# f1=open('','r')
# f10=f1.readlines()
# f2=open('','r')
# f20=f2.readlines()

time0=time.time()
num01=''
for i in range(random.randint(300,1000)):
    num01+=str(random.randint(0,9))
num02=''
for i in range(random.randint(300,1000)):
    num02+=str(random.randint(0,9))
result=big_number_add(num01,num02)
time2=time.time()
print(len(str(result)),result,sep=' ')
print(time2-time0)