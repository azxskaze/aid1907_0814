'''大数乘法'''
from functools import reduce
from  big_add import big_add
import time
import random

tim1=time.time()
'''要用到大数加法'''
num1=''
for i in range(random.randint(11600,11700)):
    num1+=str(random.randint(0,9))
num2=''
for i in range(random.randint(11600,11700)):
    num2+=str(random.randint(0,9))
tim2=time.time()
num1=str(num1)
num2=str(num2)
str01=str(num1)
str02=str(num2)
list_result_sum=[]
num01=0
n=0
for i in str01[::-1]:
    str_result='0'*n
    num02=0
    num01 = 0
    for j in str02[::-1]:
        num00=int(i)*int(j)+num01
        num01=num00//10
        num02=num00%10
        str_result+=str(num02)
        del num00
    str_result += str(num01)
    list_result_sum.append(str_result)
    del str_result
    del num01
    n+=1
print(list_result_sum)
list_sum=[]
for i in list_result_sum:
    list_sum.append(i[::-1])
print(list_result_sum)
print(list_sum)
# sum=reduce(big_add,list_sum)

print('long:',len(sum))
print('sum:',sum)
time3=time.time()
sun=int(num1)*int(num2)
print(len(str(sun)),sun)
time4=time.time()
print('*big',(time3-tim2),'**',(time4-time3))




