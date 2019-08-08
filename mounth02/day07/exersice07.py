list01=[[0,1,2,3,4,5],
        [1,28,45,6,7],
        [20,45,67,9,4]]
list02=[]
list01_len=[]
for item in list01:
    list01_len.append(len(item))
max01=max(list01_len)
for i in range(max01):
    list02.append([])
for n in range(len(list01)):
    for k in range(len(list01[n])):
        list02[k].append(list01[n][k])

for item in list02:
    print(item)
