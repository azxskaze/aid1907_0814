def my_len(list):
    count=0
    for item in list:
        count+=1
    return count
list01=[1,2,3,4,5]

str01='safdse'
print(my_len(list01),my_len(str01))

def my_max(list):
    for i in range(len(list)-1):
        if int(list[i])>int(list[i+1]):
            list[i],list[i+1]=list[i+1],list[i]
    return list[len(list)-1]
print(my_max(list01))

def my_min(list):
    for i in range(len(list)-1):
        if int(list[i])<int(list[i+1]):
            list[i],list[i+1]=list[i+1],list[i]
    return list[len(list)-1]
print(my_min(list01))

def my_sum(list):
    sum=0
    for item in list:
        sum+=item
    return sum
print(my_sum(list01))

def my_insert(list,count,chr):
    list.append([])
    # print(list_info[len(list_info)-1])
    for i in range(len(list)-1,-1,-1):
        if i > count:
            list[i],list[i-1]=list[i-1],list[i]
    list[count]=chr
list02=[111,2,3,4,5,6]
my_insert(list02,2,'a')
print(list02)

