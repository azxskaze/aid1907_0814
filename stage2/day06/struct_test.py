import  struct
# >>> st = str
# str(    struct
# >>> st = struct.Struct('i4sf')
# >>> data = st.pack(1,b'Abby',1.6)
# >>> data
# b'\x01\x00\x00\x00Abby\xcd\xcc\xcc?'
# >>> st.unpack(data)
# (1, b'Abby', 1.600000023841858)
# >>>
s1 = struct.Struct('i5s')
# data=b's'
data=(85,'ww')
a=s1.pack(*data)
print(a)
# print('%s'%a.decode().strip(b'\x00'.decode()))