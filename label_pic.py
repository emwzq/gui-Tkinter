from tkinter import *

root = Tk()
photo = PhotoImage(file="fengjing.gif")
theLabel = Label(root,
                 text="学Python\n到FishC",
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 font=("幼圆", 20),
                 fg="white")
theLabel.pack(fill=BOTH,expand=1)

mainloop()