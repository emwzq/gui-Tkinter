from tkinter import *

'''
    获取输入框里边的内容，可以使用Entry组件的get()方法。
    当然也可以将一个Tkinter的变量(通常是StringVar)挂钩到textvariable选项，
    然后通过变量的get()方法获取！！
'''

root = Tk()
e = Entry(root)
e.pack(padx=20, pady=20)
e.delete(0, END)
e.insert(0, "默认字体...")

mainloop()