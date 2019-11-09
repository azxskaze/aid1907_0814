import hashlib
m = hashlib.md5()
a = m.update(b'sjaoi')
print(a.hexdigest())