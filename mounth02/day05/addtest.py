sum=0
for item in range(10, 51):
    if item%10!=3 and item%10!=6 and item%10!=9:
        sum+=item
print(sum)