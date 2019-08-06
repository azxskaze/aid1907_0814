list01=[]
while True:
    i=input()
    if i=='':
        break
    else:
        list01.append(i)
print(''.join(list01))


a=1
b=1
print(a)
for i in range(15):
    a,b=b,b+a
    print(a)


