# print(str((1,2)).encode())
# list1 = ['1','2']
# print('*'.join(list1))
import hashlib
hash = hashlib.md5()
hash.update('%4$'.encode())
a = hash.hexdigest()
print(a)
# str1 = '%^&$%^&%^&$%^&%^&$%^&%^&$%^&'
# password = 'jiodsf'
# list1 = []

# print(''.join(list1))
while True:
    str1 = '%^&$%^&%^&$%^&%^&$%^&%^&$%^&'
    list1 = []
    password = input(':')
    for i in range(len(str1)):
        list1.append(str1[i])
        try:
            list1.append(password[i])
        except:
            print(''.join(list1))
            hash = hashlib.md5()
            hash.update((''.join(list1)).encode())
            a = hash.hexdigest()
            print(a)
            break

