from tkinter import *

master = Tk()
master.geometry('100x400+500+100')
scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(master, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=listbox.yview)
mainloop()
