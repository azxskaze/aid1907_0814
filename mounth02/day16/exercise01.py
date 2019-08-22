import time
# def fun(year,mounth,day):
#     time_tuple=time.strptime('%d/%d/%d'%(year,mounth,day),'%Y/%m/%d')
#     print('第%s周'%time_tuple[6])
# fun(2019,8,21)
# 输入年月日求星期几

def fun01(year,mounth,day):
    time_tuple = time.strptime('%d/%d/%d' % (year, mounth, day), '%Y/%m/%d')
    s=time.time()-time.mktime(time_tuple)
    print(int(s/24/60/60),'天')
fun01(1996,12,1)
# 输入年月日求年龄