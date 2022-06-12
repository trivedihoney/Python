import random

#You will guess computer chosen number
def guess(x):
    random_number = -1
    while random_number != x:
        random_number = int(input("Your Guess : \n"))
        if random_number < x:
            print(f"Guess {random_number} too low")
        elif random_number > x:
            print(f"Guess {random_number} too high")
        else:
            print(f"Your guess {random_number} is correct!!")


# guess(random.randint(0, 100))

#Computer will guess your chosen number
def computer_guess():
    print("Guess a number between 0 to 10000\n")
    min_guess = 0
    max_guess = 10000
    n=0
    guessed_number = False
    while guessed_number != "C":
        guessed_number_val = random.randint(min_guess, max_guess)
        n+=1
        guessed_number = (input(f"is {guessed_number_val} correct? Or is your guess higher or lower? C/H/L\n")).upper()
        if guessed_number == "H":
            min_guess = guessed_number_val+1
        elif guessed_number == "L":
            max_guess = guessed_number_val-1
        elif guessed_number != "C":
            print("Please choose from C/H/L")

    print("Yay!", guessed_number_val, "is your guess!!!\n It only took", n, "Guesses! Hehe")

computer_guess()
