#!/usr/bin/python
from tkinter import *
class App:
    def __init__(self,root):
        # frame = Frame(root)
        # frame.pack()
        self.hi = Button(text = 'say hello',bg = "green",fg = "red",command = self.say_hi)
        self.hi.pack(side=LEFT)
    def say_hi(self):
        print('awsl')
if __name__ == '__main__':
    root = Tk()
    app = App(root)
    # app.say_hi()
    root.mainloop()

