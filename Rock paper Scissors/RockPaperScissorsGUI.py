import random
from tkinter import *
from tkinter import messagebox


def CheckWin(PressedBtnText):
    computerChoice= c = random.choice(["r","p","s"])
    p= PressedBtnText
    if PressedBtnText==computerChoice:
        messagebox.showinfo("Result", "It's a Draw") 
    elif (p=="r" and c=="s") or (p=="s" and c=="p") or (p=="p" and c=="r"):
        messagebox.showinfo("Result","You Win!!") 
    else:
        messagebox.showinfo("Result","You Lost!!") 

root=Tk()

Rock =Button(text="Rock",font=("Arial",40), command= lambda : CheckWin("r"))
Rock.pack(fill=X)
Paper =Button(text="Paper",font=("Arial",40) ,command=lambda : CheckWin("p"))
Paper.pack(fill=X)
Scissors =Button(text="Scissors",font=("Arial",40),command=lambda : CheckWin("s"))
Scissors.pack(fill=X)



root.mainloop()