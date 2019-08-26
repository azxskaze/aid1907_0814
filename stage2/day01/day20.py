import time
# list01=[i for i in range(1000000)]
# a=time.time()
# list01.insert(1,50)
# b=time.time()
# print(b-a)
def insert_time(num):
    list01=[i for i in range(num)]
    a = time.time()
    list01.insert(1, 50)
    b = time.time()
    print(b-a)
insert_time(100000000)