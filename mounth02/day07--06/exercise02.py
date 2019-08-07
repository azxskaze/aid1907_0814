tuple_mounth=(31,28,31,30,31,30,31,31,30,31,30,31)
year=int(input())
mounth=int(input())
day=int(input())
day+=sum(tuple_mounth[:mounth-1])
# day+=tuple_mounth.sum(0,mounth-1)
print(day)
if mounth>2 and year%4==0 and year%100!=0 or year%400==0:
    day+=1
print(day)
