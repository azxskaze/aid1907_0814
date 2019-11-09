from PIL import Image

def plus(str):
    return str.zfill(8)

def get_key(strr):
    tmp = strr
    f = open(tmp,'rb')
    str = ''
    s = f.read()
    for i in range(len(s)):
        print(s[i])
        str = str+plus(bin(s[i]).replace('0b',''))
    f.close()
    print(str)
    return str
get_key('key.txt')
# def mod(x,y):
#     return x%y

