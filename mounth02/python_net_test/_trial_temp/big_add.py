from functools import reduce
def big_add(num1,num2):
    str01 = str(num1)
    str02 = str(num2)
    str03 = str()
    if len(str01) > len(str02):
        str02 = '0' * (len(str01) - len(str02)) + str02
    elif len(str02) > len(str01):
        str01 = '0' * (len(str02) - len(str01)) + str01
    print(str01, str02)
    num01 = 0
    for j in range(len(str02) - 1, -1, -1):
        num00 = int(str01[j]) + int(str02[j]) + num01
        num01 = num00 // 10
        num02 = num00 % 10
        str03 += str(num02)
    return str03[::-1]

# print(reduce(big_add,(1254,25840,3654)))
# print(1254+25840+3654)
# print(big_add(12,12))


