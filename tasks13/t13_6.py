from tkinter import *
class HelloClass:
    # create the window in the class constructor
    def __init__(self):
        widget = Button(None, text='Press Me to quit', command=self.quit)
        widget.pack()

    def quit(self):
        print('leaving now')
        import sys ; sys.exit()

HelloClass()	# create a HelloClass object
mainloop()
