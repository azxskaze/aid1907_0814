# mounth=int(input('mounth'))
# if mounth>12 or mounth<1:
#     print('输入有误')
# elif mounth==1 or mounth==3 or mounth==5 or mounth==7 or mounth==8 or mounth==10 or mounth==12:
#     print(31)
# elif mounth==2:
#     print(28)
# else:
#     print(30)
year=int(input('plz'))
day=29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
print(day)
