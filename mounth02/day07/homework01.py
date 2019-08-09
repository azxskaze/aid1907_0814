list01 = [

    [0,1,2,3,4],
    [1,28,45,6,7],
    [20,7,3,65,2]

]

def matrix_change(list):
    list01=[]
    # length=[]
    # for x in list:
    #     length.append(len(x))
    # # max_length = max(length)
    # for y in range(max_length):
    #     list01.append([])
    for i in range(len(list)):
        list01.append([])
        for j in range(len(list)):
            list01[i].append(list[j][i])
    return list01



list02=matrix_change(list01)
for item in list02:
    for i in item:
        print(i,end=' ')
    print()