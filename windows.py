from tkinter import *
def showTable(): 
    root = Tk()
    im = PhotoImage(file='Images/table.png')
    l = Label(root, image=im)
    l.pack()
    root.mainloop()
    return