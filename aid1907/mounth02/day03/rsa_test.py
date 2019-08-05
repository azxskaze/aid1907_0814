'''n=p*q
φ(n)=(p-1)*(q-1)=(11-1)*(13-1)=120
e*d≡1 mod φ(n)
c=m**e mod n

e是一个随机数（1--φ(n)之间）且e与φ(n)互质
d=e^-1
'''
import random
import math


# print(2**2049)
# item=random.randint(1e+200,1e+241)
# j=random.randint(1e+200,1e+241)
# k=random.randint(1e+200,1e+241)
# m=int(str(item)+str(j)+str(k))
# n=str(m)
# print(len(n),'\n',n)
# item=2
def big_num():
    h=0
    print('第',h,'次')
    h+=1
    i = random.randint(1e+2, 1e+5)
    j = random.randint(1e+2, 1e+5)
    k = random.randint(1e+2, 1e+5)
    m = int(str(i) + str(j) + str(k))
    n=2
    while True:
        if m%n==0:
            print('no')
            big_num()
        n+=1
        print(n)
        if n**2>m:
            return m
            break
    else:
        return  m

# print('big:',big_num())
def sushu(n):
    m=2
    while True:
        if n%m==0:
            print('no')
            break
        m+=1
        if m**2>n:
            print('yes')
            break
sushu(big_num())







