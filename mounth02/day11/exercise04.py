# noinspection SpellCheckingInspection
class Skill:
    def __init__(self,name,scale,time,ap):
        self.name=name
        self.scale=scale
        self.time=time
        self.ap=ap
    def show(self):
        print('mane:%s,scale:%s,time:%s,ap:%s'%(self.name,self.scale,self.time,self.ap))

    @property
    def scale(self):
        return self.__scale
    @scale.setter
    def scale(self,value):
        if 0.1<=value<=5:
            self.__scale=value
        else:
            raise ValueError('erro')

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, value):
        if 0.1 <= value <= 10:
            self.__time = value
        else:
            raise ValueError('erro')

    @property
    def ap(self):
        return self.__ap
    @ap.setter
    def ap(self, value):
        if 0 <= value <= 100:
            self.__ap = value
        else:
            raise ValueError('erro')

list01 = [Skill('镖',2,2,0),
        Skill('闪',1,5,30),
        Skill('影',2,3,30),
        Skill('斩',4,4,0),
        Skill('降龙十八掌',5,5,100)
        ]

def find(name):
    for item in list01:
        if item.name == name:
            return item
def no_ap():
    list02 = []
    for item in list01:
        if item.ap == 0:
            list02.append(item)
    return list02
def find_name_and_time():
    list=[]
    for item in list01:
        dict01={}
        dict01['name'] = item.name
        dict01['time'] = item.time
        list.append(dict01)
    return list
def delete():
    count=0
    for item in range(len(list01)-1,-1,-1):
        if list01[item].ap==0:
            del list01[item]
            count+=1
    if count:
        print('删除%d个'%count)
    else:
        print('删除失败')

def find_big():
    for item in range(len(list01)-1):
        if list01[item].scale>list01[item+1].scale:
            list01[item],list01[item+1]=list01[item+1],list01[item]
    return list01[len(list01)-1]

def maopao():

    for i in range(len(list01)-1):
        for j in range(len(list01)-i-1):
            if list01[j].time>list01[j+1].time:
                list01[j],list01[j + 1]=list01[j+1],list01[j]
maopao()
for i in list01:
    i.show()



find('降龙十八掌').show()
list_no_ap =  no_ap()
for item in list_no_ap:
    print('no_ap')
    item.show()
list03=find_name_and_time()
print(list03)
delete()
for i in list01:
    i.show()

find_big().show()

