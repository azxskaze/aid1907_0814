a=['1']
b=['2']
def fun(a,b):
    a[:]='2'
    
    temp=b[:]
    temp='1'
fun(a,b)
print(a,b)