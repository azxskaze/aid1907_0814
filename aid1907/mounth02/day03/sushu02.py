def extend(num):
    for iten in range(2,num):
        if num % iten == 0:
            break
    else:
        return num
def get_prime(begin,end):
    return [i for i in range(begin,end) if extend(i) ]
print(get_prime(3,50))



