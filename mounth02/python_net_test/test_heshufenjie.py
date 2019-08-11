num0=int(input('plz'))
print(num0,'=',sep='',end='')
list01=list()
num01=num0
for i in range(2,num01//2):
    if num01%i==0:
        list01.append(i)
        print(i,'*',sep='',end='')
        num01/=i
list01.append(int(num01))
print(int(num01))

