from re import A, M
from words import words
import tkinter
import random
import string

def getRandomWord():
    word = random.choice(words)

    while "-" in word or " " in word :
        word = random.choice(words)
    return word.upper()


def playHangman():
    word = getRandomWord()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7

    while len(word_letters)>0 and lives>0 :
        print(f"You have {lives} live left. and you have used letters : {', '.join(used_letters)}")
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input("\nGuess a letter :").upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')
        else:
            print('\nThat is not a valid letter.')

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


playHangman()




