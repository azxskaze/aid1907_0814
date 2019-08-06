#
# i = float(input('plz key money:'))
# money=0
# if i>100:
#     money+=(i-100)*0.01
#     i=100
# if i>60:
#     money+=(i-60)*0.015
#     i=60
# if i>40:
#     money+=(i-40)*0.03
#     i=40
# if i>20:
#     money+=(i-20)*0.05
#     i=20
# if i>10:
#     money+=(i-10)*0.075
#     i=10
# money+=i*0.1
# print(money)


'''用列表和循环做利润（麻烦）'''
i = int(input('plz key money:'))
sum=0
list01=[0,10,20,40,60,100]
list02=[0.1,0.075,0.05,0.03,0.015,0.01]
for item in range(1,6):
    if i >= list01[item]:
        sum += (list01[item]-list01[item-1])*list02[item-1]
    else:
        item-=1
        break
sum += (i-list01[item])*list02[item]
print(sum)




