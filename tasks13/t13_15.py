from tkinter import *
top = Tk()
def helloCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello World")
B = Button(top, text ="Hello", command = helloCallBack)
B.pack()
B.place(bordermode=OUTSIDE, height=100, width=100)
top.mainloop()
