from tkinter import *

class ScrolledList(Frame):
    def __init__(self,options,parent=None):
        Frame.__init__(self,parent)
        self.pack(expand=YES, fill=BOTH)
        self.makeWidgets(options)

    def handleList(self,event):
        index = self.list.curselection()
        label = self.list.get(index)
        self.runCommand(label)

    def makeWidgets(self, options):
        sbar = Scrollbar(self)
        list = Listbox(self,relief=SUNKEN)
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, expand=YES, fill=BOTH)
        pos = 0
        for label in options:
            list.insert(pos,label)
            pos += 1
        #list.config(selectmode=SINGLE, setgrid = 1)
        list.bind('<Double-1>', self.handleList)
        self.list = list

    def runCommand(self,selection):
        print('You selected ' , selection)
        
if __name__ == '__main__' :
    options = map((lambda x : 'My Choice - ' + str(x)) , range(20))
    ScrolledList(options).mainloop()
