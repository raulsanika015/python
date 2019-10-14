from tkinter import *#importing all classes from tkinter
root = Tk( )#creating instance of window
root.title("A simple window")#name of window
root.geometry('250x250+50+50')#width height x and y position to display
B1=Button(root,text="one",relief=GROOVE)
B1.pack()
B2=Button(root,text="two")
B2.pack()
B3=Button(root,text="three")
B3.pack()

root.mainloop( )#most imp to start window
