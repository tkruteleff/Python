import random

options = ["low", "High", "Exact"]
number_to_guess = random.randint(1,9)
number_of_guesses = 0
user_guess = 0

while user_guess != number_to_guess:
    user_guess = int(input("Guess a number between 1 and 9: "))

    if user_guess > number_to_guess:
        print(options[1])
        number_of_guesses += 1
    elif user_guess < number_to_guess:
        print(options[0])
        number_of_guesses += 1
    else:
        print(options[2])
        number_of_guesses += 1
        print("You guessed the number in", number_of_guesses,"turns")
        break
