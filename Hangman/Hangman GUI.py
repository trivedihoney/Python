from cProfile import label
from tkinter import *
from tkinter import ttk
import string
import random
from tkinter import font
from Hangman.Hangman import playHangman
from words import words
from PIL import Image, ImageTk


word_list_label = Label(text="", font=(48))
word_list_label.grid(row =4 , column=0,columnspan=13)

def get_valid_word():
    word = random.choice(words)
    while " " in word or "-" in word:
         word = random.choice(words)
    return word

def PlayHangman():
    word = get_valid_word()
    all_letters = set(string.ascii_letters)
    word_letters = set(word)
    
    word_list = ["-" if letter in word_letters else letter for letter in word]
    print(word_list)


def BtnPressed(a):
    pass


lives = 6
root = Tk()

letters =list(set(string.ascii_letters.upper()))
letters.sort()
Livestext = Label(text=f"Lives Left : {lives}", font=(24))
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

i=0
for x in range(5,7):
    for y in range(0, 13):

        exec(f"{letters[i]} = ttk.Button(text='{letters[i]}', style = 'my.TButton',width=3, command = lambda a=letters[i]: BtnPressed(a))")
        exec(f"{letters[i]}.grid(row={x},column={y})")
        if i+1 <len(letters) : i+=1


playHangman()
root.mainloop()