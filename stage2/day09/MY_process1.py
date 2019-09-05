from multiprocessing import Process
import time
class MyProcess(Process):
    def __init__(self,star,stop):
        self.star = star
        self.stop = stop

        super().__init__()

    def run(self):
        def my_time(fun):
            def pack(*args, **kwargs):
                a = time.time()
                print('kaishi', a)
                b = fun(*args, **kwargs)
                print('jieshu')
                print(time.time() - a)
                return b
            return pack
        star = self.star
        stop = self.stop
        @my_time
        def zhishu(star,stop):
            sum = 0
            for i in range(star, stop):
                for j in range(2, i):
                    if i % j == 0:
                        break
                    else:
                        continue
                else:
                    sum += i
            print(sum)
            return sum
        return zhishu(self.star,self.stop)
list1 = []
list2 = []
for i in range(2,100000,25000):
    p = MyProcess(i,i+25000)
    a=p.start()
    list2.append(a)
    list1.append(p)
for i in list1:
    i.join()
for i in list2:
    print(i)



