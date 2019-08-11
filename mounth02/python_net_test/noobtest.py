# m**2=x+100
# n**2=x+268
# n**2-m**2=168
# print(100**2-99**2)
for i in range(100):
    for j in range(i,100):
        if j**2-i**2==168 :
            print(i**2-100,j**2-268)

