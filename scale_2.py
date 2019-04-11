from tkinter import *

root = Tk()
Scale(root, from_=0, to=42).pack()
Scale(root, from_=0, to=200, orient=HORIZONTAL).pack()

mainloop()

from tkinter import *

root = Tk()
Scale(root, from_=0, to=666, tickinterval=5, length=200, resolution=3, orient=VERTICAL).pack()
Scale(root, from_=0, to=200, tickinterval=10, length=600, orient=HORIZONTAL).pack()

mainloop()