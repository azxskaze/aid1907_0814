list01=[1,2,3,4]
list02=[i+1 for i in  list01 if i%2]
print(list02)
'''列表推导式'''
dict01={1:'a',2:'b'}
dict02={k:v  for k,v in dict01.items()}
print(dict02)
'''字典推导式'''
list01=[i**2 for i in range(1,11)]
list02=[i for i in list01 if i%2]
list03=[i for i in list01 if i%2==0]
print(list01,'\n',list02,'\n',list03,sep='')
'''列表推导式的嵌套'''
list04=[i+i1 for i in list02 for i1 in list03]
print(list04)
list03.append()



