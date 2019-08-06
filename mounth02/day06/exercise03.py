list01 = list('abc')
print(id(list01[2]))
list01[:2] = [0,1,2]
print(list01)
print(id(list01[3]))


list02=[1,2,3]
print(list02 is list02[:])
