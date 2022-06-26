import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
img=""


root= Tk()
root.title(" ")
root.geometry('200x200')
#img = ImageTk.PhotoImage(Image.open(f"Dice rolling simulator/1.png"))
diceImg = Label(root)
diceImg.pack(ipady=25)


def RollDice():
    global img
    dice = random.randint(1,6)
    img = ImageTk.PhotoImage(Image.open(f"Dice rolling simulator/{dice}.png"))
    diceImg.configure(image=img)


RollBtn = ttk.Button(text ="Roll the dice", command= RollDice)
RollBtn.pack(side=BOTTOM,fill=X)


root.mainloop()