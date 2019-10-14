from tkinter import *
from tkinter import Label
top=Tk()
top.geometry('200x200')
ent=Entry(top,bd=5)
ent.pack()
lbl=Label(top,text="Enter only a number")
lbl.pack()
def reader():
     v=int(ent.get())
     if v%2==0:
          lbl.config(text=str(v)+" is even")
     else:
          lbl.config(text=str(v)+" is odd")
     return

btn=Button(top,text="Read",command=reader)
btn.pack()
top.mainloop()
