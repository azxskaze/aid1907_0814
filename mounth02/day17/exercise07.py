list1=[10,12,5,62,43,5,3,11]
def biger_10(list):
    list02=[]
    for item in list:
        if item>10:
            list02.append(item)
    return list02

def ibiger_10(list):
    for item in list:
        if item>10:
            yield item
list02=list(ibiger_10(list1))
print(list02)
