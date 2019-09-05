'''
100000以内质数之和:
单进程'''
# 25.806628227233887
# 454396537
import time
def my_time(fun):
    def pack(*args,**kwargs):
        a=time.time()
        b=fun(*args,**kwargs)
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
    return sum

a=zhishu(2,100000)
print(a)