#!/usr/bin/python
from tkinter import *
root = Tk()

root.title("标题")
# listbox组件
label1 = Label(root,text='静态文本',justify = LEFT,padx = 100)
label1.pack()

listb = Listbox(root)
listb.pack()
li = [1,2,3]
for i in li:
    listb.insert(True,i)
theButton = Button(root,text='删除',command=lambda x=listb:x.delete(ACTIVE))
theButton.pack()

root.mainloop()

