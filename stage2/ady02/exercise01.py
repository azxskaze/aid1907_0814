'''逆波兰表达式'''
class StrackError(Exception):
    pass

class Strack:
    def __init__(self):
        self.__elems = []
    def is_null(self):
        return self.__elems == []
    def push(self,i):
        # for i in list(value):
        self.__elems.append(i)
    def pop(self):
        if self.__elems:
            return  self.__elems.pop()
        else:
            raise StrackError
    def top(self):
        if self.__elems:
            return  self.__elems[-1]
        else:
            raise StrackError
# import sys
# print(sys.path)
# list01=[12,10,'+',4,'-',12,'*',6,'/','p']
# list01=[1,2,'+',3,'-','p']
str1=input('plz')
list01=str1.split(' ')
print(list01)
s1=Strack()
for i in range(len(list01)):
    if str(list01[i]) in '+-*/':
        s1.push(list01[i-2])
        s1.push(list01[i-1])
    
    if str(list01[i]) == '+':
        a=s1.pop()
        b=s1.pop()
        c=int(b)+int(a)
        s1.push(c)
        list01[i]=c
    elif str(list01[i]) == '-':
        a = s1.pop()
        b = s1.pop()
        c = b - a
        s1.push(c)
        list01[i] = c
    elif str(list01[i]) == '*':
        a = s1.pop()
        b = s1.pop()
        c = b * a
        s1.push(c)
        list01[i] = c
    elif str(list01[i]) == '/':
        a = s1.pop()
        b = s1.pop()
        c = b / a
        s1.push(c)
        list01[i] = c
    elif str(list01[i]) == 'p':
        print(s1.top())
        print(list01)


