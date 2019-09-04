# def a(numRows):
#     list=[]
#     if numRows == 0:
#         return
#     elif numRows >= 1:
#         list.append([1])
#     for i in range(2, numRows + 1):
#         list.append([])
#         for j in range(i):
#             if j == 0:
#                 list[i-1].append(list[i-2][j])
#             elif j == i-1:
#                 list[i-1].append(list[i-2][j-1])
#             else:
#                 list[i-1].append(list[i-2][j]+list[i-2][j-1])
#     return list
# a(5)
class Struck:
    def __init__(self):
        self.list=[]
    def add(self,chr):
        self.list.append(chr)
    def pop(self):
        return self.list.pop()
    def show(self):
        if self.list == []:
            return False
        return self.list[-1]
def cc(source):
    s1 = Struck()
    str1 = '\n'.join(source) + ' '
    list2 = []
    i=0

    while i<len(str1)-1:
        if str1[i]+str1[i+1] == '//':
            i += 2
            if s1.list == []:
                s1.add('//')
        elif str1[i] == '\n':
            i+=1
            if s1.show() == '//':
                s1.pop()
            else:
                list2.append('\n')
        elif  str1[i]+str1[i+1] == '/*':
            i += 2
            if s1.list == []:
                s1.add('/*')

        elif str1[i]+str1[i+1] == '*/':
            i += 2
            if s1.show() == '/*':
                s1.pop()

        else:
            i += 1
            if s1.list == []:
                list2.append(str1[i-1])
    list3=''.join(list2).strip().strip('').split('\n')
    for i in range(len(list3)-1,-1,-1):
        if list3[i] == '':
            del list3[i]
    print(list3[3] == '')
    return list3
list1=["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
print(cc(list1))
