sun_home=['水星','金星','地球','火星','木星','土星','天王星','海王星']
print('距离太阳最近的行星是：%s'%sun_home[0])
print('距离太阳最远的行星是：%s'%sun_home[len(sun_home)-1])
print('太阳到地球之间的有%s'%sun_home[:2])
for star in sun_home:
    print(star)
print(sun_home[::-1])
for star in range((len(sun_home)-1),-1,-1):
    print(sun_home[star])
