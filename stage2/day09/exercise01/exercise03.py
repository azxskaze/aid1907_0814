import time
import multiprocessing as mp
def my_time(fun):
    def pack(*args,**kwargs):
        a=time.time()
        print('kaishi',a)
        b=fun(*args,**kwargs)
        print('jieshu')
        print(time.time()-a)
        return b
    return pack
@my_time
def zhishu(star,stop):
    sum=0
    for i in range(star,stop):
        for j in range(2,i):
            if i % j == 0:
                break
            else:
                continue
        else:
            sum += i
    print( sum )
list1 = []
star = 2
end = 100000
step = 10000
for i in range(star,end,step):
    p = mp.Process(target=zhishu,args=(i,i+step))
    list1.append(p)
    p.start()
for i in list1:
    i.join()




