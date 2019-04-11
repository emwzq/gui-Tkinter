from tkinter import *

'''
    Entry组件还支持验证输入内容的合法性。例如输入框要求输入的是数字，用户输入了字母就属于非法输入。
    实现该功能，需要通过设置validate，validatecommand和invalidcommand三个选项。
    其次是为validatecommand选项指定一个验证函数，该函数只能返回True或False表示验证结果。
    一般情况下验证函数值需要知道输入框的内容即可，可以通过Entry组建的get（）方法获得改字符串
'''

root = Tk()

def test():
    if e1.get() == "123456":
        print("正确")
        return True
    else:
        print("错误！")
        # e1.delete(0, END)
        return False

v = StringVar()
e1 = Entry(root, textvariable=v,
            #validate="focus",
            # validate="focusout",
            validate="all",
           validatecommand=test)
e2 = Entry(root)
e1.pack(padx=10, pady=10)
e2.pack(padx=10, pady=10)

mainloop()