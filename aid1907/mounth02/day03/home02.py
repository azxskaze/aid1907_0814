age = int(input('plz key age:'))
if age < 0:
    print('erro')
elif age < 2:
    print('婴儿')
elif age < 13:
    print('儿童')
elif age < 20:
    print('青年')
elif age < 65:
    print('成年人')
elif age < 130:
    print('老年人')
else:
    print('那不可能')