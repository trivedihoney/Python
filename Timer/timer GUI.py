from cProfile import label
from cgitb import text
from telnetlib import X3PAD
from tkinter import *
from tkinter import ttk

root= Tk()
hour=StringVar()
minute=StringVar()
second=StringVar()
root.title = "Timer"
root.geometry('{}x{}'.format(500, 250))
Progressbar = ttk.Progressbar()
Progressbar.pack(fill=X)
frameFiller= Frame(root,width=500,height=50)
frameFiller.pack()
frameX= Frame(root,width=500)
frameX.pack()

tbhours = Entry(frameX,font=('Arial',48,'bold'),width=2,textvariable=hour)
tbhours.pack(side=LEFT)
label1 = Label(frameX, text="  :  ")
label1.pack(side=LEFT)
tbminutes = Entry(frameX,font=('Arial',48,'bold'),width=2,textvariable=minute)
tbminutes.pack(side=LEFT)
label2 = Label(frameX, text="  :  ")
label2.pack(side=LEFT)
tbseconds = Entry(frameX,font=('Arial',48,'bold'),width=2,textvariable=second)
tbseconds.pack(side=LEFT)

frame2=Frame(root,bg="BLACK",width=500,height=100)
frame2.pack(side=BOTTOM)
StartBtn = Button(frame2,text="Start Timer",bg="Green")
StartBtn.pack(fill=BOTH,expand=True,ipadx=500,ipady=15)
root.mainloop()