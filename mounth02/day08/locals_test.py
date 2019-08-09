'''locals()
将局部变量存储到一个以变量名为键对应的值为值的字典中去'''
def people():
    name='a'
    age=12
    weight=55
    return locals()
print(people()['name'])
