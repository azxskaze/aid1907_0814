import random
import math
list01=[]
list02=[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]

def sushu():
    i=3
    while len(list01)<53:
        j=2
        while True:
            if i%j==0:
                break
            if j**2>i:
                list01.append(i)
                break
            j+=1

        i+=1
    k=1
    for item in list01:
        print(item,end=' ')
        if k%5==0:
            print()
        k+=1
    print(len(list01))
    print(list01)



sushu()


