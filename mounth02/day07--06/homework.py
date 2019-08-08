# dict01={
#     '北京':{'美食':['烤鸭','豆汁','卤煮','炸酱面'],
#            '景区':['故宫','天安门','天坛']},
#
#     '四川': {
#             '美食': [ '火锅', '串串', '毛血旺'],
#             '景区': ['峨眉山', '九寨沟', '春熙路']}
# }
# for key in dict01:
#     print(key,':')
#     for item in dict01[key]:
#         print('  ',item,':',end='')
#         for i in dict01[key][item]:
#             print(i,end=' ')
#         print()
# beijing_meishi=dict01['北京']['美食']
# for item in beijing_meishi:
#     print(item,end=' ')


        # for i in item:
        #     print('  ',i,':',end=' ')
        #     for n in item[i]:
        #         print(n,end=' ')
        #     print()




# dict02={}
# str01='this is a tese string'
# for i in str01:
#     if i not in dict02:
#         dict02[i]=1
#     else:
#         dict02[i]+=1
# print(dict02)

dict02={}
str01='this is a tese string'
for i in str01:
    dict02.setdefault(i,0)
    dict02[i]+=1
print(dict02)


