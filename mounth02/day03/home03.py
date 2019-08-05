height = float(input('身高：'))
weight = float(input('体重：'))
bmi = weight/height**2
if bmi < 18.5:
    print('体重过低')
elif bmi < 24:
    print('正常')
elif bmi < 28:
    print('超重')
elif bmi < 30:
    print('I度肥胖')
else:
    print('.....')
