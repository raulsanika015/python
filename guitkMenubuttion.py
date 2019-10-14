from tkinter import *

top = Tk()

mb =  Menubutton ( top, text = "Menu Top", relief = RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
option1  = IntVar()
option2   = IntVar()

mb.menu.add_checkbutton ( label = "option1",
                          variable = option1 )
mb.menu.add_checkbutton ( label = "option2",
                          variable = option2 )
mb.getvar(str(option1.get()))

mb.pack()
top.mainloop()
