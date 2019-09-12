# 156145
# 156651
# 155551
#
# 135812326425
#
# 135812218531
# 135811118531
# 135813318531
# print(135812626425-135812218531)
# print(135812626425-135811118531)
# print(135812626425-135813318531)

def fun(n):
    if int(n) <= 10:
        return int(n)-1
    if int(n) == '11':
        return 9
    a = len(n)
    c = a//2
    if a%2:
        q = n[:c]
        z = n[c]
        h = q[::-1]
        num2 = q+str(int(z)-1)+h
        num3 = q+str(int(z)+1)+h
        def min_i(i, a):
            print(i,a)
            if i > a:
                return i-a
            else:
                return a-i

        min2 = min_i(int(n), int(num2))
        min3 = min_i(int(n), int(num3))
        if min2 <= min3:
            return num2
        else:
            return num3

    else:
        q = n[:c]

        num2 = str(int(q)-1)+str(int(q)-1)[::-1]
        num3 = str(int(q)+1)+str(int(q)-1)[::-1]
        def min_i(i,a):
            if i > a:
                return i-a
            else:
                return a-i
        min2 = min_i(int(n), int(num2))
        min3 = min_i(int(n), int(num2))
        if min2 <= min3:
            return num2
        else:
            return num3
print(fun('1000'))

