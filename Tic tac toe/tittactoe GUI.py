from cProfile import label
from tkinter import *
from tkinter import messagebox

def ButtonClick(id):
    if id==1:
        messagebox.showinfo("Click info",f"Button {id} Clicked")        
        Btn1["text"]="O"
root = Tk()
root.title("Tic Tac Toe")



Btn1=Button(root,command=lambda : ButtonClick(1))
Btn1.grid(row=0,column=0,ipadx=50,ipady=50)
Btn2=Button(root)
Btn2.grid(row=0,column=1,ipadx=50,ipady=50)
Btn3=Button(root)
Btn3.grid(row=0,column=2,ipadx=50,ipady=50)
Btn4=Button(root)
Btn4.grid(row=1,column=0,ipadx=50,ipady=50)
Btn5=Button(root)
Btn5.grid(row=1,column=1,ipadx=50,ipady=50)
Btn6=Button(root)
Btn6.grid(row=1,column=2,ipadx=50,ipady=50)
Btn7=Button(root)
Btn7.grid(row=2,column=0,ipadx=50,ipady=50)
Btn8=Button(root)
Btn8.grid(row=2,column=1,ipadx=50,ipady=50)
Btn9=Button(root)
Btn9.grid(row=2,column=2,ipadx=50,ipady=50)


statusbar = Label(root, text="It's O's Turn",bd=1,anchor=W)
statusbar.grid(row=3,column=0,columnspan=3)
statusbar2 = Label(root, text="O wins : ",bd=1,anchor=W)
statusbar2.grid(row=4,column=0)
statusbar3 = Label(root, text="X wins :",bd=1,anchor=W)
statusbar3.grid(row=4,column=2)

BtnRestart = Button(root,text="RESTART")
BtnRestart.grid(row=4,column=1)

root.mainloop()