def maopao(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
list01=[1,5,8,7,2,9,4,3,6]
print(maopao(list01))
