p1Input = str(input("Player 1 choose either rock, paper or scissors: "))
p2Input = str(input("Player 2 choose either rock, paper or scissors: "))

def compare(p1, p2):
    if p1 == p2:
        print("You picked the same answer!")
    elif p1 == "rock":
        if p2 == "scissors":
            return("Player one wins!")
        else:
            return("Player two wins!")
    elif p1 == "scissors":
        if p2 == "paper":
            return("Player one wins!")
        else:
            return("Player two wins!")
    elif p1 == "paper":
        if p2 == "rock":
            return("Player one wins!")
        else:
            return("Player two wins!")
    else:
        sys.exit()

print(compare(p1Input, p2Input))
