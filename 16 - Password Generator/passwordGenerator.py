import random
#Write a password generator in Python.
#Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
#The passwords should be random, generating a new password every time the user asks for a new password.
#Include your run-time code in a main method.

#Extra:
#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

chars = list(range(ord('a'),ord('z')+1))
chars += list(range(ord('A'),ord('Z')+1))
chars += list(range(ord('0'),(ord('9')+1)))
chars += list(range(ord('!'),ord('&')+1))

dictionary = ["word", "input", "list", "end", "order", "rock", "paper", "scissors"]
password = ""

passwordStrength = str(input("Do you want a weak or strong password? "))

def generateWeak(list):
    generated = random.choices(dictionary, k=2)

    return (password.join(generated))

def generateStrong(keys):
    key = []
    for i in range(16):
        key.append(chr(keys[random.randint(0,len(keys)-1)]))

    return (password.join(key))

if passwordStrength == "weak":
    print(generateWeak(dictionary))
elif passwordStrength == "strong":
    print(generateStrong(chars))
else:
    print("sigh")
