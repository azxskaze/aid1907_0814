list01=[[0,1,2,3,4],
        [1,28,45,6,7],
        [20,45,67,9,4]]
for item in list01[1]:
    print(item,end=' ')
print()

for item in list01:
    for i in range(len(item)):
        if i==0:
            print(item[i])

for item in list01:
    for i in item:
        print(i,end=' ')
    print()
