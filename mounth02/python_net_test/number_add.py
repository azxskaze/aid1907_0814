import random
import time
time0=time.time()
num01=''
for i in range(random.randint(300,400)):
    num01+=str(random.randint(0,9))
num02=''
for i in range(random.randint(300,400)):
    num02+=str(random.randint(0,9))
print(int(num01)+int(num02))
time1=time.time()
print(time1-time0)
print(666*666)