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
                if int(self.__stu_list[j].scores)>int(self.__stu_list[j+1].scores):
                    self.__stu_list[j],self.__stu_list[j+1]=self.__stu_list[j+1],self.__stu_list[j]
class StudentManagerView:
    stu_list = StudentManagerController()
    # def __init__(self):
    #     pass
    # '''显示菜单'''

    def __display_menu(self):
        menu='''
+----------------------------+
| 1） 添加学生信息             |
| 2）显示学生信息              |
| 3）删除学生信息              |
| 4）修改学生信息              |
| 5）按学生成绩低~高显示学生信息 |
+----------------------------+
                '''
        print(menu)
        '''选择菜单项'''

    def main(self):
        while True:
            self.__display_menu()
            while True:
                i=int(input('请选择：'))
                if i in (1,2,3,4,5):
                    break
            self.__select_menu_item(i)
            n=input('继续？（y/n）')
            if n=='y':
                continue
            else:
                break

    def __select_menu_item(self,i):

        if i==1:
            self.__input_students()
        elif i==2:
            self.__output_students()
        elif i==3:
            self.__delete_student()
        elif i==4:
            self.__modify_student()
        else:
            self.__upup()

    def __input_students(self):
        name=input('name')
        age=input('age')
        score=input('score')
        self.stu_list.add_student(StudentModel(name,age,score))
        # print(self.__manager.__manager[0].name)
    def __output_students(self):
        for i in self.stu_list.stu_list:
            i.show()
    def __delete_student(self):
        id=int(input('请输入学号'))
        self.stu_list.remove_student(id)
    def __modify_student(self):
        id=int(input('请输入要修改学生的学号：'))
        name=input('请输入要修改学生的新姓名：')
        age=int(input('请输入要修改学生的新年龄：'))
        score=int(input('请输入要修改学生的新成绩：'))
        self.stu_list.update_student(StudentModel(name,age,score,id))
    def __upup(self):
        self.stu_list.sort_student()



#
# list01=StudentManagerController()
# stud01=StudentModel(5,6,9)
# stud05=StudentModel(5,6,1)
# stud02=StudentModel(5,6,12)
# stud03=StudentModel(5,6,88)
# list01.add_student(stud01)
# list01.add_student(stud02)
# list01.add_student(stud03)
# list01.add_student(stud05)
#
# # print(list01.update_student(StudentModel('a',9,8,stud01.id)))
#
#
# list01.sort_student()
# for i in list01.__manager:
#     i.show()
if __name__=='__main__':
    manager=StudentManagerView()
    manager.main()



