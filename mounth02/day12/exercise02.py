class Preson():
    def __init__(self,name,money):
        self.name = name
        self.money = money

    def teach(self,obj,skill):
        print(self.name,'教',obj.name,skill)
        # obj.learn(skill)

    # def learn(self,skill):
    #     print(self.name,'学',skill)

    def work(self,num):
        print(self.name,'上班挣了',num)
        self.money += num

zwj = Preson('张无忌',0)
zm = Preson('赵敏',0)

zwj.teach(zm,'乾坤大挪移')
zm.teach(zwj,'化妆')
zwj.work(10000)
zm.work(6000)
