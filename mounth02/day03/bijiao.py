# num01=int(input('num01:'))
# num02=int(input('num02:'))
# if num01<num02:
#     print(num02)
# else:
#     print(num01)
'''三个数比较'''

temp=0
num01=int(input('num01:'))
num02=int(input('num02:'))
num03=int(input('num03:'))
temp=num01
if temp<num02:
    temp=num02
if temp<num03:
    temp=num03
print(temp)