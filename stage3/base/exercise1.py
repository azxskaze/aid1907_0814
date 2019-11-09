import base64
import json
a = base64.b64encode(b'chenwenxing')
b = base64.b64decode(a)
print(a,b.decode())
header={'alg':'H256','typ':'JWT'}
str1 = json.dumps(header)
print(str1.encode()+b'.')
import hashlib
import hmac
s = hashlib.sha256()
s.update(b'123456')
s2 = s.digest()
s3 = s.hexdigest()
print(type(s),s)
endcoding='gb18030'
print(type(s2),s3,int(s3,16))

# 加盐的哈希算法
h = hmac.new(b'qwert',b'123456',digestmod='SHA256')
print(h.hexdigest())
a = b'sa.sd'
print(a.split(b'.'))




