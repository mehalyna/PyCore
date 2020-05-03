from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

def callback():
    print(e.get())

b = Button(master, text="get", width=10, command=callback)
b.pack()
mainloop()
