'''希尔排序'''
import random
import time

from stage2.ady02 import maopao


def xier(list01):
    long=int(len(list01)/2)
    for i in range(long):
        if list01[i]>list01[i+long]:
            list01[i],list01[i + long]=list01[i+long],list01[i]
            '''先用分组思想分成len/2组进行交换'''
    # for i in range(len(list01)):
    #     for j in range(len(list01)-1):
    #         if list01[j]<=list01[i]<=list01[j+1]:
    #             str1=list01[i]
    #             list01.insert(str1,j)
    #             del list01[i+1]
    '''再用插入排序'''
    # print('分组排序完毕')
    # for i in range(len(list01)):
    #     for j in range(i,0,-1):
    #         if list01[j]<list01[j-1]:
    #             list01[j],list01[j - 1]=list01[j-1],list01[j]
    for i in range(len(list01),4):
        if list01[i]>list01[i+1]:
            list01[i],list01[i + 1]=list01[i+1]>list01[i]
        if list01[i+2]>list01[i+3]:
            list01[i+2],list01[i + 3]=list01[i+3]>list01[i+2]

'''希尔排序20000长度随机序列排序用时25.6
   插入排序20000长度随机序列排序用时
   冒泡排序20000长度随机序列排序用时27.5'''
if __name__=='__main__':
    list01 = [random.randint(0, 100000) for i in range(20000)]
    a = time.time()
    xier(list01)
    # maopao.maopao(list01)
    # maopao.order_insert(list01)
    print(list01)
    print(time.time()-a)
