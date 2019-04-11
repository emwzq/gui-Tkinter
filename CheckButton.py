from tkinter import *

root = Tk()
GIRLS = ["西施", "王昭君", "貂蝉", "杨玉环"]
v = []

def check():
    for i in v:
        if i.get() == True:
            print (i.get())

for girl in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root, text=girl, variable=v[-1],command=check)
    b.pack(anchor=W)

mainloop()