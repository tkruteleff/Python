import random

options = ["low", "High", "Exact"]
numberToGuess = random.randint(1,9)
numberOfGuesses = 0
userGuess = 0

while userGuess != numberToGuess:
    userGuess = int(input("Guess a number between 1 and 9: "))

    if userGuess > numberToGuess:
        print(options[1])
        numberOfGuesses += 1
    elif userGuess < numberToGuess:
        print(options[0])
        numberOfGuesses += 1
    else:
        print(options[2])
        numberOfGuesses += 1
        print("You guessed the number in", numberOfGuesses,"turns")
        break
