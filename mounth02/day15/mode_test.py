class  S:
    def c(self):
        print('c')
class A(S):
    def a(self):
        print('121212')

class B(A):
    pass
b=B()
b.a()
b.c()
a=A()
a.c()