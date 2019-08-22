list01=['孙悟空','白雪公主','贾宝玉']
list02=[101,102,103]
# for item in zip(list01,list02):
#     print(item)
def my_zip(list1,list2):
    for i in range(len(list1)):
        yield (list1[i],list2[i])


for i in my_zip(list01,list02):
    print(i)
