class Iter1:
    def __init__(self,data):
        self.__data=data
        self.i=-1
    def __next__(self):
        if self.i>=len(self.__data)-1:
            raise StopIteration
        self.i+=1
        return self.__data[self.i]




class EmployeeManager:
    def __init__(self):
        self.__employee_list=[]
    def add_employee(self,person):
        self.__employee_list.append(person)
    def __iter__(self):
        return Iter1(self.__employee_list)

employee=EmployeeManager()
employee.add_employee('张无忌')
employee.add_employee('张翠山')
employee.add_employee('张三丰')


for item in employee:
    print(item)

# employeeiter=employee.__iter__()
# while True:
#     try:
#         item=employee.__next__()
#     except StopIteration:
#         break


