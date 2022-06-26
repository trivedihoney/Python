import random

def playgame():
    playerChoice = input('Choose any one option\n"r" for Rock, "p" for paper, "s" for sciossors\n')
    while playerChoice!= "r" and "p" and "s":
        print("Invalid choice")
        playerChoice = input('Choose any one option:\n"r" for Rock, "p" for paper, "s" for sciossors\n')
    
    computerChoice = random.choice(["r","p","s"])
    #print (computerChoice)
    #r>s,s>p,p>r
    result =isWin(playerChoice,computerChoice)
    print(result)

def isWin(p,c):
    if p==c:
        return "It's a Draw"
    elif (p=="r" and c=="s") or (p=="s" and c=="p") or (p=="p" and c=="r"):
        return "You Win!!"
    else:
        return "You Lost!!"

playgame()