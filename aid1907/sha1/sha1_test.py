str1='abc'
list1 = []
for i in str1:
    list1.append(bin(ord(i)))
list2=[]
for i in list1:
    i=i.replace('0b','')
    if len(i)<8:
        for j in range(8-len(i)):
            i='0'+i
    list2.append(i)
# print(list2)
# 原始数据长度
len1=len(list2)*8
x=((len1)+1)%512
if x<448:
    y=448-x
elif x>448:
    y=512-(x-448)
else:
    y=0
list2.append('1')
print(x,y)
print((x+y)%512)
for i in range(y):
    list2.append('0')
str2=''.join(list2)
# print(len(str2)%512,str2)

# nu=int(str2,2)
# print(nu,'\n',int(str(nu),16))
list3=[]
for i in range(0,len(str2),8):
    list3.append(str2[i:i+8])
print(list3)
list16=[]
for i in range(0,len(list3),4):

    # print(i1)
    # print(int(list3[i]+list3[i+1]+list3[i+2]+list3[i+3],2))
    k=hex(int(list3[i]+list3[i+1]+list3[i+2]+list3[i+3],2))
    k=k.replace('0x','')
    if len(k) == 8:
        list16.append(k)
    else:
        for n in range(8-len(k)):
            k='0'+k
        list16.append(k)

# print(len(list16),list16)
len16 = str(hex(len1)).replace('0x','')
for i in range(16-len(len16)):
    len16 = '0'+len16
print(type(len16))
for i in range(0,len(len16),8):
    list16.append(len16[i:i+8])
'''到这一步预处理就完了'''
print(len(list16),list16)
str3=''.join(list16)


t=0
if 0<=t<=19:
    kt=0x5A827999
elif 20 <= t <= 39:
    kt=0x6ED9EBA1
elif 40 <= t <= 59:
    Kt = 0x8F1BBCDC
elif 60 <= t <= 79:
    kt=0xCA62C1D6

def ft(B,C,D):
    if 0 <= t <= 19:
        return (B & C) | ((~ B) & D)
    elif 20 <= t <= 39:
        return B ^ C ^ D
    elif 40 <= t <= 59:
        return (B & C) | (B & D) | (C & D)
    elif 60 <= t <= 79:
        return B ^ C ^ D

H0 = 0x67452301
H1 = 0xEFCDAB89
H2 = 0x98BADCFE
H3 = 0x10325476
H4 = 0xC3D2E1F0





