list01=[]
while True:
    i=input()
    if i=='':
        break
    else:
        list01.append(i)
print(''.join(list01))


fibs=[0,1]
for i in range(15):
    fibs.append(fibs[i]+fibs[i+1])
print(fibs)


