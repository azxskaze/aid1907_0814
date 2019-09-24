import random
def maopao(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j+1],list[j]=list[j],list[j+1]
'''插入排序'''

def order_insert(list01):
    for i in range(len(list01)):
        for j in range(i,0,-1):
            if list01[j]<list01[j-1]:
                list01[j],list01[j - 1]=list01[j-1],list01[j]

def a(l,i,j):
    x=l[i]
    while i < j:
        if l[j] < x:
            l[i],l[j]=l[j],l[i]
            j-=1
    while i < j:
        if l[i] > x:
            l[i],l[j] = l[j],l[i]
            i+=1
    return i

def kuaisu(l, i, j):
    if i < j:
        key = a(l, i, j)
        kuaisu(l, i, key)
        kuaisu(l, key, j)



l=[5,4,6,2,7,6,9,1]
# l=[1,4,2]
kuaisu(l,i=0,j=len(l)-1)
print(l)


# list01 = [random.randint(0, 100000) for i in range(2000)]
# order_insert(list01)
#
# print(list01)

