i = 100
while i < 1000:
    if (i % 10)**3+(i//10%10)**3+(i//100)**3==float(i):
        print(i)
    i+=1