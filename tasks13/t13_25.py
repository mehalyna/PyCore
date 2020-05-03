from tkinter import *

class SliderDemo(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        self.var = IntVar()
        Scale(self,label='Miles', command=self.onMove, variable = self.var, from_=0, to=100,length=200, tickinterval=20).pack()
        Button(self , text='Read', command=self.readScale).pack(pady=10)

    def onMove(self, value):
        print('onMove = ' , value)

    def readScale(self):
        print('readscale = ' , self.var.get())

if __name__== '__main__' :
    SliderDemo().mainloop()
