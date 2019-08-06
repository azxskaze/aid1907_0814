'''多态'''
class Animal:
    def say(self):
        return '..'

class dog(Animal):
    def say(self):
        return 'wang'
class cat(Animal):
    def say(self):
        return 'miao'
gou=dog()
mao=cat()
animal=Animal()
print(animal.say())
print(gou.say())
print(mao.say())
