year=int(input('year:'))
mounth=int(input('mounth:'))
day=int(input('day:'))
i=1
day_all=0
while i<mounth:
    if i == 2 :
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            day_all += 29
        else:
            day_all += 28

    if i ==4 and i == 6 and i == 9 and i == 11:
        day_all+=30
    else:
        day_all += 31
    i+=1
day_all+=day
print(day_all)

