import time
l=19
c=0
while True:
    print('\r%s@%s'%('#'*c,'#'*(l-c)),end='')
    # try:
    time.sleep(0.3)
    # except KeyboardInterrupt:
    #     print('\nBye-bye')
    #     break
    if c==l:
        c=0
    c+=1