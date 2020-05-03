from tkinter import *

def cb():
    print("variable is", var.get())

win = Tk()
var = IntVar()
c = Checkbutton(win, text="Enable Tab", variable=var, command= (lambda: cb()))
c.pack()

mainloop()
