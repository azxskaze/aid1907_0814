''''''
'''列表的优缺点
优点：增删查改很快，有序可以索引切片
缺点：数据量大的时候查找慢，代码可读性差'''
'''字典的优缺点
优点：查找速度快，数据较多时通过k-v查找代码可读性高
缺点：无序，不能索引，占用内存大'''
'''根据需求结合本身的优缺点综合考虑'''
dict01={}
while True:
    dict02={}
    name=input('name')
    if name=='':
        for item in dict01:
            print('%s的年龄是%s,性别是%s,体重是%s.'
                  %(item,dict01[item]['age'],
                    dict01[item]['gender'],dict01[item]['weight']))
        break
    age=input('age')
    dict02['age']=age
    gender=input('gender')
    dict02['gender'] = gender
    weight = input('weight')
    dict02['weight'] = weight
    dict01[name]=dict02


