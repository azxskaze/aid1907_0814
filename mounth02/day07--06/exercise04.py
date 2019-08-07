dict01={}
while True:
    name=input('plz key name')
    if name=='':
        for item in dict01:
            print(item,'的价格是',dict01[item])
            if item=='游戏机':
                print('\n游戏机的价格是：',dict01[item],sep='')
        break
    price=input('plz key price')
    dict01[name] = price





