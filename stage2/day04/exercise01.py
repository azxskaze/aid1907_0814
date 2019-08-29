''''''
f=open('/home/tarena/PycharmProjects/aid1907/stage2/dict.txt','r')

# dict01={}
# for line in f:
#     list01=line.split(' ')
#     dict01[list01[0]]=list01[1:-1]
#
# f.close()
# while True:
#     world = input('plz key a world:')
#     if world in dict01:
#         print(' '.join(dict01[world]))
#     else:
#         print('no')
# print(dict01)

for i in f:
    k=input('请输入要查找的单词：')
    if i>k:
        '''遍历的单词已经大于要找的单词说明已经找不到了'''
        print('no')
        break
    if k ==i.split(' ')[0]:
        print(''.join(i[1:-1]))
        break
    else:
        print('no')
f.close()




