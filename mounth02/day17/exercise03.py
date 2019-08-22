class Iter1():
    def __init__(self,stop,star,step):
        self.star = star
        self.stop = stop
        self.step = step
        self.i=self.star-self.step
    def __next__(self):
        if self.i>=self.stop-self.step:
            raise StopIteration
        self.i+=self.step
        return self.i

class MyRange:
    def __init__(self,*args):
        if len(args)==1:
            self.star = 0
            self.stop = args[0]
            self.step = 1
        elif len(args)==3:
            self.star=args[0]
            self.stop=args[1]
            self.step=args[2]
    def __iter__(self):
        return Iter1(self.stop,self.star,self.step)
# class MyRange:
#     def __init__(self,star=0,stop=0,step=1):
#         self.star=star
#         self.stop=stop
#         self.step=step
#     def __iter__(self):
#         return Iter1(self.stop,self.star,self.step)
'''循环一次，计算一次，返回一次，之前的数据都被回收了'''
for item in MyRange(2,100,3):
    print(item)
# iter1=MyRange(5).__iter__()

# while True:
#     try:
#         item=iter1.__next__()
#         print(item)
#     except StopIteration:
#         break
