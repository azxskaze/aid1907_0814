# import random
# l1=[1,2,3,5]
# list1=[]
# def combination(l):
#     if l == []:
#         return ''
#     for i in l:
#         a1=i
#         yield a1,combination(l[1:len(l)])
#
#
#
# def ex_combination(l):
#     for i in l:
#         print(i[0])
#         if type(i[1]) == 'generator':
#             return ex_combination(i)
#
# ex_combination(combination(l1))

# ex_combination(l)
# l=combination(l1)
# for i,j in l:
#     print(i)
#     for k in j:
#         print(k[0])
#         for n in k[1]:
#             print(n)




# for n in range(len(l)):
#     for i in range(len(l)):
#         l[n] = i

# '''排列'''
# from itertools import product
# l = [1, 2, 3]
# print (list(product(l, l)))
# print (list(product(l, repeat=3)))
# '''组合'''
# from itertools import combinations
# l = {1, 2, 3, 6, 5}
# print (list(combinations(l, 4)))
# from itertools import product
# from itertools import combinations
import itertools
'''''
 生成排列
 列表中元素不允许重复出现
 排列数计算为：n！，其中n为num_list列表中元素个数
 '''
import time
def test_func1(s, words):
    a=time.time()
    list2=[]
    tmp_list = itertools.permutations(s)
    for i in tmp_list:
        # str2=''.join(['%s'%j for j in i])
        str2=''.join(i)
        # str2=str(str2)
        # words=str(words)
        # if  str2 in words:
        #     list2.append(words.index(str2))
        len1=len(str2)
        len2=len(words)
        for i in range(len2-len1):
            if words[i:len2].startswith(str2):
                list2.append(i)
    print(time.time()-a)
    return list2



str11 = "barfoothefoobarman"
l=["foo","bar"]
# l=[1,3,5]
l1=test_func1(l,str11)
print(l1)