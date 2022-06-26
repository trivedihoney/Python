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

# get_proper_word
def get_proper_word():
    word = random.choice(words)
    while " " in word or "-" in word:
         word = random.choice(words)
    return word.upper()



root = Tk()
root.configure(background="white")
lives = IntVar(root,6)

word = get_proper_word()
all_letters = set(string.ascii_letters.upper())
word_letters = set(word)
guessed_letters = set()



letters =list(set(string.ascii_letters.upper()))
letters.sort()

Livestext = Label(text=f"Lives Left : {lives.get()}", font=("Arial", 40),bg="white")
Livestext.grid(row=0,column=0,columnspan=13,ipady=10)

img = ImageTk.PhotoImage(Image.open(f"Hangman/{lives.get()}.PNG").resize((640,360),Image.Resampling.LANCZOS))
GifLabel = Label(root,image=img)
GifLabel.grid(row=1,column=0,columnspan=13)



word_list = ["_" if letter in word_letters else letter for letter in word]
word_list_label = Label(root,text="   ".join(word_list), font=("Arial",40), bg="white")
word_list_label.grid(row =3 , column=0,columnspan=13,ipady=50)
s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 24))
style = ttk.Style()
style.configure("Gr.TButton",font=('Helvetica', 24), foreground="Green")
style2 = ttk.Style()
style2.configure("Red.TButton",font=('Helvetica', 24), foreground="Red")
style3 = ttk.Style()
style3.configure("Reset.TButton",font=('Helvetica', 24))

i=0
for x in range(5,7):
    for y in range(0, 13):

        exec(f"{letters[i]} = ttk.Button(text='{letters[i]}', style = 'my.TButton',width=3, command = lambda a=letters[i]: BtnPressed(a))")
        exec(f"{letters[i]}.grid(row={x},column={y})")
        if i+1 <len(letters) : i+=1

def BtnPressed(btn_letter):

    print (btn_letter)
    
    if btn_letter in word_letters:
        exec(f"{btn_letter}.configure(style = 'Gr.TButton')")
        word_letters.remove(btn_letter)
        word_list = ["_" if letter in word_letters else letter for letter in word]
        word_list_label.config(text="  ".join(word_list))
        if len(word_letters)<1:
            messagebox.showinfo("WIN",'Yay!!! You guessed the word!!')
            guessed_letters.clear()
            resetAll()

    elif btn_letter in guessed_letters:
        pass
    elif btn_letter in letters:
        global img
        num = lives.get()
        num-=1
        lives.set(num)
        Livestext.config(text=f"Lives Left : {lives.get()}")
        guessed_letters.add(btn_letter)
        exec(f"{btn_letter}.configure(style = 'Red.TButton')")
        img = ImageTk.PhotoImage(Image.open(f"Hangman/{lives.get()}.PNG").resize((640,360),Image.Resampling.LANCZOS))
        GifLabel.configure(image=img)

        if num<1:
            messagebox.showinfo("GAME OVER",f"Game Over!! The Word was {word}")
            guessed_letters.clear()
            resetAll()
    else :
        messagebox.showinfo("ERROR",'Please enter a valid letter')

def resetAll():
    global word, word_list, word_letters,img
    lives.set(6)
    Livestext.config(text=f"Lives Left : {lives.get()}")
    img = ImageTk.PhotoImage(Image.open(f"Hangman/{lives.get()}.PNG").resize((640,360),Image.Resampling.LANCZOS))
    GifLabel.configure(image=img)
    word = get_proper_word()
    word_letters = set(word)
    word_list = ["_" if letter in word_letters else letter for letter in word]
    word_list_label.config(text="  ".join(word_list))

    for btn_letter in letters:
        exec(f"{btn_letter}.configure(style = 'Reset.TButton',width=3)")


root.mainloop()