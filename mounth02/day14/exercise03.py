class System:
    def __init__(self):
        self.__staff_list=[]
    @property
    def staff_list(self):
        return self.__staff_list
    def add_staff(self,staff):
        if isinstance(staff,Staff):
            self.__staff_list.append(staff)
        else:
            raise ValueError(' ')
    def total_stall_salary(self):
        all_salary=0
        for item in self.__staff_list:
            all_salary+=item.salary()
        return all_salary
class Staff:
    def __init__(self,base):
        self.base=base
    def salary(self):
        raise NotImplementedError()
class Programmer(Staff):
    def __init__(self,base,share):
        super().__init__(base)
        # self.base=base
        self.share=share
    def salary(self):
        return self.base+self.share
class Saleswoman(Staff):
    def __init__(self,base,sales):
        super().__init__(base)
        # self.base=base
        self.sales=sales
    def salary(self):
        return self.base+self.sales*0.05

s1=Saleswoman(2000,10000)
p1=Programmer(2000,1000)
sy1=System()
sy1.add_staff(s1)
sy1.add_staff(p1)
print(sy1.total_stall_salary())