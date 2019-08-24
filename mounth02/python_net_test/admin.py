'''9.8'''
class User:
    def __init__(self,frist_name,last_name):
        self.frist_name=frist_name
        self.last_name=last_name
    def describe(self):
        print(self.frist_name,self.last_name)
    def greet_user(self):
        print('hola')
class Admin(User):
    def __init__(self,frist_name,last_name):
        self.privileges = []
        super().__init__(frist_name,last_name)
        for item in self.privileges:
            print(item)

class Privileges():
    def __init__(self):
        self.privileges=['can add post','can delete post']
    def show_privileges(self):
        for item in self.privileges:
            print(item)

p01=Privileges()
# p01.show_privileges()
admin=Admin('a','b')
admin.privileges=p01.privileges
admin.show_privileges()

