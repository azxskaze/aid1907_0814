from tkinter import *
class Test:

    def __init__(self,root):
        self.root = root
        self.fram1 = Frame(self.root)
        self.fram2 = Frame(self.root)
        self.var = StringVar()
        self.var.set('aaaaaa')

    def new(self):
        self.var.set('ssssss')

    def lab(self):
        label1 = Label(self.fram1, textvariable=self.var, justify=LEFT)
        label1.pack(side=LEFT)

    def create_button(self):
        bu = Button(self.fram2,text = 'ff',command = self.new)
        bu.pack(padx = 100,pady = 100)


    def show(self):
        self.fram1.pack(padx = 100,pady = 100)
        self.fram2.pack(padx = 100,pady = 100)


    def rdbu(self):
        v = IntVar()
        li = [1,2,3]
        li1 = [3,2,1,0]
        for i in li:
            ru = Radiobutton(self.root,text = i,variable = v,value = li1[i],indicatoron = False)
            ru.pack()

    def group1(self):
        group =  LabelFrame(self.root,text = "sss")
        group.pack()
        LANGS = [("Python", 1), ("Per1", 2), ("Ruby", 3), ("Lua", 4)]
        v = IntVar()
        v.set(1)
        for i,j in LANGS:
            b = Radiobutton(group,text = i,variable = v,value = j)
            b.pack(anchor = W)

    def text1(self):
        # 静态文本
        e = Entry(self.root)
        e.pack()
        e.delete(0,END)
        e.insert(0,'moren')

    def main(self):
        self.lab()
        self.rdbu()
        self.group1()
        self.text1()
        self.create_button()
        self.show()


root = Tk()
a = Test(root)
a.main()
mainloop()