import math
import operator
''' 
ID3练习
outlook,temperature,humidity,windy,play
'''
exercise_set=[[0,0,0,0,'n'],
          [0,0,0,1,'n'],
          [1,0,0,0,'y'],
          [2,1,0,0,'y'],
          [2,2,1,0,'y'],
          [2,2,1,1,'n'],
          [1,2,1,1,'y'],
          [0,1,0,0,'n'],
          [0,2,1,0,'y'],
          [2,1,1,0,'y'],
          [0,1,1,1,'y'],
          [1,1,0,1,'y'],
          [1,0,1,0,'y'],
          [2,1,0,1,'n'] ]
'''练习数据'''
sum=len(exercise_set)
def deep1():
    yes=0
    no=0
    for list in exercise_set:
        if list[len(list)-1]=='y':
            yes+=1
    no=sum-yes
    entropy_s=-yes/sum*math.log(yes/sum,2)-no/sum*math.log(no/sum,2)
    return entropy_s
    '''求出总的熵值'''
entropy_s=deep1()

def deep2(name,type):
    y = 0
    n = 0
    sun=0
    for list in exercise_set:
        if list[name]==type:
            if list[len(list)-1]=='y':
                y+=1
            else:
                n+=1
    sun=y+n
    if y==0 or n==0:
        entropy=0
    else:
        entropy=-y/sun*math.log(y/sun,2)-n/sun*math.log(n/sun,2)
    return [entropy,sun]

entropy_s_outlook_0=deep2(0,0)
entropy_s_outlook_1=deep2(0,1)
entropy_s_outlook_2=deep2(0,2)
entropy_s_outlook=entropy_s_outlook_0[0]*entropy_s_outlook_0[1]/sum+entropy_s_outlook_1[0]*entropy_s_outlook_1[
    1]/sum+entropy_s_outlook_2[0]*entropy_s_outlook_2[1]/sum
gaim_s_outlook=entropy_s-entropy_s_outlook

entropy_s_temperature_0=deep2(1,0)
entropy_s_temperature_1=deep2(1,1)
entropy_s_temperature_2=deep2(1,2)
entropy_s_temperature=entropy_s_temperature_0[0]*entropy_s_temperature_0[1]/sum+entropy_s_temperature_1[0]*entropy_s_temperature_1[1]/sum+entropy_s_temperature_2[0]*entropy_s_temperature_2[1]/sum
gaim_s_temperature=entropy_s-entropy_s_temperature

entropy_s_humidity_0=deep2(2,0)
entropy_s_humidity_1=deep2(2,1)
entropy_s_humidity=entropy_s_humidity_0[0]*entropy_s_humidity_0[1]/sum+entropy_s_humidity_1[0]*entropy_s_humidity_1[1]/sum
gaim_s_humidity=entropy_s-entropy_s_humidity

entropy_s_windy_0=deep2(3,0)
entropy_s_windy_1=deep2(3,1)
entropy_s_windy=entropy_s_windy_0[0]*entropy_s_windy_0[1]/sum+entropy_s_windy_1[0]*entropy_s_windy_1[1]/sum
gaim_s_windy=entropy_s-entropy_s_windy




# print('信息增益熵值为：',entropy_s,gaim_s_outlook,gaim_s_temperature,gaim_s_humidity,gaim_s_windy)


