import threading
import time
# class My(threading):
#     def __init__(self):
#         super.__init__()
#     def fun(self,n):
#         time.sleep(n / 100)
#         print(n)
#     def run(self):
def fun(n,l):
    time.sleep(n/1000)
    l.append(n)
    # print(n)
list1 = [5,6,3,89,7,22,36,41,48,999,568,236,96,54,1,268,12,3,698,669,568,759,25,364,96,65,86,61,23,12,13,16,14,15,16,
         21,22,23,24,25,26,28,29,32,36,35,52,59,]
l2 = []
l3 = []
for i in list1:
    t= threading.Thread(target=fun,args=(i,l2))
    t.start()
    l3.append(t)

for i in l3:
    i.join()

print(l2)