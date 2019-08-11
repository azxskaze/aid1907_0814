list01 = [
    [0,1,2,3,4],
    [1,28,45,6,7],
    [20,7,3,65,2]
]
list02=[[] for i in list01[0]]

for item in list01:
    for j in range(len(list02)):
        list02[j].append(item[j])
print(list02)

