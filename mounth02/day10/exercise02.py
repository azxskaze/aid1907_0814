class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def show_student(self):
        print('学生姓名%s,年龄%s,成绩%s'
        %(self.name,self.age,self.score))
# a=Student('王小明',21,90)
# b=Student('李小狼',19,95)
# c=Student('tool',10,10)
list01=[Student('王小明',21,50),Student('李小狼',19,95),Student('赵敏',20,90)]
list01[0].show_student()

def fund01(list,name):
    for item in list:
        if item.name==name:
            return item
name='王小明'
print('%s的成绩是%s'%(name,fund01(list01,name).score))

def fund02(list,age):
    list1=[]
    for item in list:
        if item.age<age:
            # return locals()
            list1.append(item)
    return list1

list02=fund02(list01,30)
if list02:
    for i in list02:
        print(i.name)

def fun03(list):
    for i in list[::-1]:
        if i.score<60:
            list.remove(i)

fun03(list01)

if list01:
    for i in list01:
        print(i.name)

