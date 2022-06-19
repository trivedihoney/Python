from ast import Global
from cProfile import label
from operator import truediv
from textwrap import fill
from tkinter import *
from tkinter import ttk

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

BtnRestart = ttk.Button(frame4,text="RESTART",style='TT.TButton')
BtnRestart.grid(row=1,column=1,columnspan=2,rowspan=2,sticky="nesw")

def ButtonClick(id):
    #messagebox.showinfo("Click info",f"Button {id} Clicked")    
    global player
    if id["text"]=="":
        id["text"]=player

        if IfGameEnd() == True:
            statusbar1.configure(text=f"It's {player}'s Turn")
        else:
            if player == "O": 
                player="X" 
            else: player = "O"            
            statusbar1.configure(text=f"It's {player}'s Turn")

Owins = {"X","X","X"}
def IfGameEnd():
    if frame1.grid[0,0]==frame1.grid[0,1]==frame1.grid[0,2]:
        print("Someone won")
        return True
    else:
        return False

def t(btn):
    return btn.cget("text")

root.mainloop()