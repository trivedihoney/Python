from ast import Global
from cProfile import label
from operator import truediv
from textwrap import fill
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
Owins=0
Xwins=0
root = Tk()
player = "O"
root.title("Tic Tac Toe")
s = ttk.Style()
s.configure('TTT.TButton', font=('Helvetica', 48))
ss = ttk.Style()
ss.configure('TT.TButton', font=('Helvetica', 12))
#root.geometry('{}x{}'.format(450, 500))

frame1=Frame(root,width=450, height=150)
frame1.grid(row=0,column=0)
frame1.grid_propagate(False)
frame1.columnconfigure(0,weight=1)
frame1.columnconfigure(1,weight=1)
frame1.columnconfigure(2,weight=1)
frame1.rowconfigure(0,weight=1)

frame2=Frame(root,width=450, height=150)
frame2.grid(row=1,column=0)
frame2.grid_propagate(False)
frame2.columnconfigure(0,weight=1)
frame2.columnconfigure(1,weight=1)
frame2.columnconfigure(2,weight=1)
frame2.rowconfigure(0,weight=1)

frame3=Frame(root,width=450, height=150)
frame3.grid(row=2,column=0)
frame3.grid_propagate(False)
frame3.columnconfigure(0,weight=1)
frame3.columnconfigure(1,weight=1)
frame3.columnconfigure(2,weight=1)
frame3.rowconfigure(0,weight=1)

Btn1=ttk.Button(frame1,command=lambda : ButtonClick(Btn1),style='TTT.TButton',)
Btn1.grid(row=0,column=0,sticky="nesw")
Btn2=ttk.Button(frame1,command=lambda : ButtonClick(Btn2),style='TTT.TButton')
Btn2.grid(row=0,column=1,sticky="nesw")
Btn3=ttk.Button(frame1,command=lambda : ButtonClick(Btn3),style='TTT.TButton')
Btn3.grid(row=0,column=2,sticky="nesw")
Btn4=ttk.Button(frame2,command=lambda : ButtonClick(Btn4),style='TTT.TButton')
Btn4.grid(row=0,column=0,sticky="nesw")
Btn5=ttk.Button(frame2,command=lambda : ButtonClick(Btn5),style='TTT.TButton')
Btn5.grid(row=0,column=1,sticky="nesw")
Btn6=ttk.Button(frame2,command=lambda : ButtonClick(Btn6),style='TTT.TButton')
Btn6.grid(row=0,column=2,sticky="nesw")
Btn7=ttk.Button(frame3,command=lambda : ButtonClick(Btn7),style='TTT.TButton')
Btn7.grid(row=0,column=0,sticky="nesw")
Btn8=ttk.Button(frame3,command=lambda : ButtonClick(Btn8),style='TTT.TButton')
Btn8.grid(row=0,column=1,sticky="nesw")
Btn9=ttk.Button(frame3,command=lambda : ButtonClick(Btn9),style='TTT.TButton')
Btn9.grid(row=0,column=2,sticky="nesw")

frame4=Frame(root,width=450,height=100)

frame4.grid(row=4,column=0)
frame4.grid_propagate(False)
frame4.columnconfigure(0,weight=1)
frame4.columnconfigure(1,weight=1)
frame4.columnconfigure(2,weight=1)
frame4.rowconfigure(0,weight=1)
statusbar1 = ttk.Label(frame4, text=f"It's {player}'s Turn",font=(48),relief=SUNKEN,width=450,anchor=CENTER,borderwidth=1)
statusbar1.grid(row=0,column=0,columnspan=3,sticky="nsew")

statusbar2 = ttk.Label(frame4, text="O wins : ",font=(24))
statusbar2.grid(row=1,column=0,sticky="nesw")
statusbar3 = ttk.Label(frame4, text="X wins :",font=(24))
statusbar3.grid(row=2,column=0,sticky="nesw")

BtnRestart = ttk.Button(frame4,text="RESTART",style='TT.TButton',command=lambda : restart())
BtnRestart.grid(row=1,column=1,columnspan=2,rowspan=2,sticky="nesw")

def ButtonClick(id):
    #messagebox.showinfo("Click info",f"Button {id} Clicked")    
    global player,Owins,Xwins
    
    if id["text"]=="":
        id["text"]=player

        if IfGameEnd() == True:
        
            statusbar1.configure(text=f"{player} Won !!!")
            messagebox.showinfo("Result", f"{player} Won !!!")
            DisableEnableBoard("disabled")
            if player == "O": 
                Owins +=1
                statusbar2.configure(text="O wins : {}".format(Owins))
            else: Xwins  +=1 ; statusbar3.configure(text="X wins : {}".format(Xwins))

        else:
            if checkDraw()==False:
                if player == "O": 
                    player="X" 
                else: player = "O"            
                statusbar1.configure(text=f"It's {player}'s Turn")
            else:
                messagebox.showinfo("Result","It's a Draw")
                DisableEnableBoard("disabled")
                statusbar1.configure(text="Draw")

def IfGameEnd():
    if t(Btn1)== t(Btn2)==t(Btn3) and t(Btn1)!="":
        return True
    elif  t(Btn4)== t(Btn5)==t(Btn6) and t(Btn4)!="":
        return True
    elif  t(Btn7)== t(Btn8)==t(Btn9) and t(Btn7)!="":
        return True
    elif  t(Btn1)== t(Btn4)==t(Btn7) and t(Btn1)!="":
        return True
    elif  t(Btn2)== t(Btn5)==t(Btn8) and t(Btn2)!="":
        return True
    elif  t(Btn3)== t(Btn6)==t(Btn9) and t(Btn3)!="":
        return True        
    elif  t(Btn1)== t(Btn5)==t(Btn9) and t(Btn1)!="":
        return True
    elif  t(Btn3)== t(Btn5)==t(Btn7) and t(Btn3)!="":
        return True
    else:
        return False

def t(btn):
    return btn.cget("text")

def DisableEnableBoard(text):
    Btn1["state"]= Btn2["state"]=Btn3["state"]= Btn4["state"]= Btn5["state"]= text
    Btn6["state"]=Btn7["state"]=Btn8["state"]=Btn9["state"]= text

def restart():
    Btn1["text"]= Btn2["text"]=Btn3["text"]= Btn4["text"]= Btn5["text"]= ""
    Btn6["text"]= Btn7["text"]=Btn8["text"]= Btn9["text"]= ""
    DisableEnableBoard("enable")

def checkDraw():
    if Btn1["text"]!="" and Btn2["text"]!="" and Btn3["text"]!="" and Btn4["text"]!="" and Btn5["text"]!="" and Btn6["text"]!="" and Btn7["text"]!="" and Btn8["text"]!="":
        return True
    else:
        return False


root.mainloop()