name='a'
def fun():
    name = 'b'
    def un():
        global name
        name='c'
        print(name)
    un()
    print(name)
fun()
print(name)