import random1
import time
time0=time.time()
num01=''
for i in range(random1.randint(600, 700)):
    num01+=str(random1.randint(0, 9))
num02=''
for i in range(random1.randint(600, 700)):
    num02+=str(random1.randint(0, 9))
result=int(num01)*int(num02)
print(len(str(result)),result)
time1=time.time()
print(time1-time0)