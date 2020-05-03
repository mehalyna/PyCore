from tkinter import *

F1 = Frame()
s = Scrollbar(F1)
L = Listbox(F1)

s.pack(side=RIGHT, fill=Y)
L.pack(side=LEFT, fill=Y)

s['command'] = L.yview
L['yscrollcommand'] = s.set

for i in range(30):
    L.insert(END, str(i))
F1.pack(side=TOP)

F2 = Frame()
lab = Label(F2)

def poll():
    lab.after(200, poll)
    sel = L.curselection()
    lab.config(text=str(sel))

lab.pack()
F2.pack(side=TOP)

poll()
mainloop()
