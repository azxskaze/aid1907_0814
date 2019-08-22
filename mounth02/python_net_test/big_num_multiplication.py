import random1
import time
from functools import reduce
from big_number_add import big_number_add
def big_number_m(num01,num02):
    global str_num01, str_num02, str_num03, num00, num0, max_len
    str_num01 = str(num01)
    str_num02 = str(num02)
    str_num03 = str()
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
    global i, num0, num00
    list01=[]
    for m in range(max_len - 1, -1, -1):
        str_num03=str()
        for i in range(max_len - 1, -1, -1):
            num0 = int(str_num01[i]) * int(str_num02[m]) + num0
            if 10 > num0:
                num00 = num0
            else:
                num00 = num0 % 10
            num0 //= 10
            str_num03 += str(num00)
        str_num03=' '*(max_len-1-m)+str_num03
        list01.append(str_num03)
        n=reduce(big_number_add,list01)
        print('**',n)
        return  n

    # print(list_info)
    # for item in list_info:
    #     '''等待'''
    # return str_num03
# num01 = float(input('请输入大整数1：'))
# num02 = float(input('请输入大整数2：'))
# f1=open('','r')
# f10=f1.readlines()
# f2=open('','r')
# f20=f2.readlines()

time0=time.time()
num01=''
for i in range(random1.randint(600, 700)):
    num01+=str(random1.randint(0, 9))
num02=''
for i in range(random1.randint(600, 700)):
    num02+=str(random1.randint(0, 9))
b=int(num01)*int(num02)
print('***',len(str(b)),b)
result=big_number_m(num01,num02)

time2=time.time()

print(len(str(result)),result,sep=' ')
print(time2-time0)