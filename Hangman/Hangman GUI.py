from ast import Global
from decimal import ROUND_DOWN
from ntpath import join
from tkinter import *
from tkinter import ttk
import string
import random
from tkinter import messagebox
from words import words
from PIL import Image, ImageTk

def get_proper_word():
    word = random.choice(words)
    while " " in word or "-" in word:
         word = random.choice(words)
    return word

word = get_proper_word()
all_letters = set(string.ascii_letters)
word_letters = set(word)
guessed_letters = set()

word_list = ["_" if letter in word_letters else letter for letter in word]
print(" ".join(word_list))


root = Tk()
lives = IntVar(root,6)
word_list_label = Label(root,text="", font=(60))
word_list_label.grid(row =4 , column=0,columnspan=13)

letters =list(set(string.ascii_letters.upper()))
letters.sort()

Livestext = Label(text=f"Lives Left : {lives.get()}", font=(24))
Livestext.grid(row=0,column=0,columnspan=13)

#img = ImageTk.PhotoImage(Image.open("Hangman/hanged.gif"))
#GifLabel = Label(root,image=img)
#GifLabel.grid(row=1,column=0,columnspan=13)

mainframe= Frame(height=500)
mainframe.grid(row=2,column=0,columnspan=13,rowspan=3)
s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 24))

def BtnPressed(btn_letter):

    print (btn_letter)
    
    if btn_letter in word_list:
        exec(f"{btn_letter}.config(bg = 'Green')")
        word_letters.remove(btn_letter)
        word_list_label.config(text="  ".join(word_list))
    elif btn_letter in letters:
        num = lives.get()
        num-=1
        lives.set(num)
        Livestext.config(text=f"Lives Left : {lives.get()}")
        if num<0:
            messagebox(f"Game Over!! The Word was {word}")
    else :
        messagebox('Please enter a valid letter')
i=0
for x in range(5,7):
    for y in range(0, 13):

        exec(f"{letters[i]} = ttk.Button(text='{letters[i]}', style = 'my.TButton',width=3, command = lambda a=letters[i]: BtnPressed(a))")
        exec(f"{letters[i]}.grid(row={x},column={y})")
        if i+1 <len(letters) : i+=1


root.mainloop()