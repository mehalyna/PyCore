from tkinter import *

root = Tk()

# To create a Tkinter variable, call the corresponding constructor
v = StringVar()
label = Label(root, textvariable = v).pack()
v.set("New Text!")
print(v.get())
root.mainloop()
