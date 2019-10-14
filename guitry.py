from tkinter import *
top = Tk()
CheckVar1= IntVar()
Cb= Checkbutton(top, text = "Music", variable = CheckVar1,onvalue = 1, offvalue = 0, height=5,width = 20,)
Cb.pack()
top.mainloop()

