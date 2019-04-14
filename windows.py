from tkinter import *
import player
def showTable(): 
    root = Tk()
    frame = Frame(root)    #используем фрейм для позиционирования
    frame.grid()
    frame = Frame(root)    #используем фрейм для позиционирования
    frame.grid() 
    title = Label(frame, text="Что по игрокам?")
    output = Text(frame, width=45, height=3)    #создаём поле вывода
    output.grid(row=10, columnspan=9)
    output.insert(2.0,player.qplayers)
    root.mainloop()
    return