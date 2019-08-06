
list01=[3,45,8,12,36,7,3]
list03=[]
for item in list01:
    if item>10:
        list03.append(item)
print(list03)

max_value=list01[0]
for item in list01:
    if item>max_value:
        max_value=item
print(max_value,list01)
'''删除特定条件元素时一定要从右往左，不然会出错，
删掉元素后会左移导致漏掉和越界'''

list02=[3,45,8,12,36,7,3]
for i in range(len(list02)-1,-1,-1):
    if list02[i]%2==1:
        del list02[i]
print(list02)

