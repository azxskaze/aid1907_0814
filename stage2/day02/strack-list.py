# class Node:
#     def __init__(self,val,index=None):
#         self.val=val
#         self.index=index
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
if __name__ == '__main__':
    st=Strack()
    print(st.is_null())
    st.push([1,5,8,9,5])
    st.pop()
    print(st.top())





