import  random
i=0
random_num=random.randint(1,10)
print(random_num)
print(type(random_num))
while True:
    i+=1
    if i>3:
        break
    num=int(input('plz:'))
    if num == random_num:
        print('you right!')
        print('你猜了',i,'次')
        break
    elif num > random_num:
        print('bigger')
    else:
        print('litter')
