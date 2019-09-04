import time

with open('log.txt','r+',buffering= 1 ) as f:
    i=0
    for line in f:
        i+=1
    t=0

    while t<=60:
        f.write(str(i+1)+'.'+' '+time.ctime()+'\n')
        f.flush()
        time.sleep(1)
        t+=1
        i+=1
f.close()


