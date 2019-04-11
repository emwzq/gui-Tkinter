from tkinter import *

root = Tk()
LANGS = [("Python", 1), ("Per1", 2), ("Ruby", 3), ("Lua", 4)]
v = IntVar()
v.set(1)
def disp():
    print ("Current = ",v.get())

for lang, num in LANGS:
    #b = Radiobutton(root, text=lang, variable=v, value=num)
    #b.pack(anchor=W)
    b = Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False,command=disp)
    b.pack(fill=X)

mainloop()