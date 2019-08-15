class StudentModel:

    def __init__(self,name,age,scores,id=0):
        self.id=id
        self.name=name
        self.age=age
        self.scores=scores
    def show(self):
        print(self.id,self.name,self.age,self.scores)


class StudentManagerController:
    __stu_id=1000
    def __init__(self):
        self.__stu_list=[]
    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self,stud):
        stud.id=self.__generate()
        self.__stu_list.append(stud)

    def __generate(self):
        StudentManagerController.__stu_id += 1
        return  StudentManagerController.__stu_id

    def remove_student(self,id):
        # count=0
        # for item in range(len(self.__stu_list)-1,-1,-1):
        #     if id==self.__stu_list[item].id:
        #         del self.__stu_list[item]
        #         count+=1
        # if count:
        #     print('成功',count,'次')
        #     return True
        # else:
        #     print('失败')
        #     return False
        for item in self.__stu_list:
            if item.id==id:
                self.__stu_list.remove(item)
                return True
        return False
    def update_student(self,stu):
        for item in self.__stu_list:
            if item.id==stu.id:
                item.name=stu.name
                item.age=stu.age
                item.scores=stu.scores
                return True
        raise ValueError('no')
    
    def sort_student(self):
        for i in  range(len(self.__stu_list)-1):
            for j in range(len(self.__stu_list) - 1-i):
                if self.__stu_list[j].scores>self.__stu_list[j+1].scores:
                    self.__stu_list[j],self.__stu_list[j+1]=self.__stu_list[j+1],self.__stu_list[j]

list01=StudentManagerController()
stud01=StudentModel(5,6,9)
stud05=StudentModel(5,6,1)
stud02=StudentModel(5,6,12)
stud03=StudentModel(5,6,88)
list01.add_student(stud01)
list01.add_student(stud02)
list01.add_student(stud03)
list01.add_student(stud05)

# print(list01.update_student(StudentModel('a',9,8,stud01.id)))


list01.sort_student()
for i in list01.stu_list:
    i.show()




