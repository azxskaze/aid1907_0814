# 对列表切片的操作不会影响到列表本身
def a(l):
    for i in range(len(l)):
        l[i]=0
l = [1,2,3,4,5]
# a(l[:3])
# print(l)

def search(l:list,key):
    low = 0
    height = len(l) - 1

    while low <= height:
        i = (height + low) // 2
        if type(l) == int:
            return l
        if l[i] == key:
            return i
        elif l[i] < key:
            low=i
        else:
            height=i
print(search(l,4))
