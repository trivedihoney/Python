import random


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


guess(random.randint(0, 100))
