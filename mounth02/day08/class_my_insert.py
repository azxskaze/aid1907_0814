
class My_Insert:
    def __init__(self,list1):
        self.list1=list1
    #     self.count=count
    #     self.chr1=chr1
    def my_insert(self,count,chr1):
        self.list1.append([])
        for i in range(len(self.list1) - 1, -1, -1):
            if i > count:
                self.list1[i], self.list1[i - 1] = self.list1[i - 1], self.list1[i]
        self.list1[count] = chr1
list02=[1,2,3,4]
m=My_Insert(list02)
m.my_insert(2,'a')
print(list02)

