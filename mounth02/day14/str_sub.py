# class Str:
#     def __init__(self,s):
#         self.s=s
#
#     def __str__(self):
#         return '%s'%self.s
#
#     def __sub__(self, other):
#         return Str(self.s.replace(other,''))

# s=Str('abcde')
# print(s)
# print(s-'abc')

# class Str01(str):
#     def __sub__(self, other):
#         return Str01(self.replace(other,''))
# s=Str01(123)
# d=Str01(2)
# print(s-d)
class List:
    def __init__(self,l):
        self.l=l
    def __str__(self):
        return ''.join(self.l)

    def __sub__(self, other):

        # list01=self.split(' ')
        return List(' '.join(self.l).replace(' '+other,''))
# list01=[1,2,3,4]
l=List(['a8','b45','c12','d98','ef'])
print(l-'b45')