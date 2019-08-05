mounth = int(input('plz key mounth:'))
if mounth < 1 and mounth >12:
    print('erro')
elif mounth > 9:
    print('冬天')
elif mounth > 6:
    print('秋天')
elif mounth > 3:
    print('夏天')
else:
    print('春天')
