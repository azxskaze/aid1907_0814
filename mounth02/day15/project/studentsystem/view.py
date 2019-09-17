from project.studentsystem.control import StudentManagerController
from project.studentsystem.model import StudentModel


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
            i.top()
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
