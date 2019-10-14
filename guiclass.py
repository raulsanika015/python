from tkinter import *

top=Tk()
top.geometry('250x250')
def printer():
     print('clicked')
     return
b=Button(top,text='click me',command=printer,bg='red')
b.pack()
top.mainloop()
