from tkinter import *

def cb():
    print("beer is", var1.get())
    print("Wine is", var2.get())
    print("Water is", var3.get())

win = Tk()
f = Frame(relief=RAISED , borderwidth=5)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

c1 = Checkbutton(f, text="Beer", variable=var1, command= (lambda: cb()))
c1.pack(side=TOP)
c2 = Checkbutton(f, text="Wine", variable=var2, command= (lambda: cb()))
c2.pack(side=TOP)
c3 = Checkbutton(f, text="Water", variable=var3, command= (lambda: cb()))
c3.pack(side=TOP)

f.pack()
mainloop()
