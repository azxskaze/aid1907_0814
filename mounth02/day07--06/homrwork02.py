dict01={}
while True:
    city=input('city:')
    dict02={}
    if city=='':
        break

    while True:
        food_post=input('美食或者景点')
        if food_post=='':
            break

        list01 = []
        while True:
            item=input('菜名或者地名')
            if item =='':
                break

            list01.append(item)
        dict02[food_post] = list01
    dict01[city] = dict02
print(dict01)



