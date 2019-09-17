class StudentModel:

    def __init__(self,name,age,scores,id=0):
        self.id=id
        self.name=name
        self.age=age
        self.scores=scores
    def show(self):
        print(self.id,self.name,self.age,self.scores)
