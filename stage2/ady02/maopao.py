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

list01 = [random.randint(0, 100000) for i in range(20000)]


