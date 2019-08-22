list1=['张无忌','张翠山','张三丰']
def my_enumerate(list):
    i=0
    for item in list:

        i += 1
        yield (i,item)

for i in my_enumerate(list1):
    print(i)