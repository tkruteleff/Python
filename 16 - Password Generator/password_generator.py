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

password_strength = str(input("Do you want a weak or strong password? "))

def generate_weak(list):
    generated = random.choices(dictionary, k=2)

    return (password.join(generated))

def generate_strong(keys):
    key = []
    for i in range(16):
        key.append(chr(keys[random.randint(0,len(keys)-1)]))

    return (password.join(key))

if password_strength == "weak":
    print(generate_weak(dictionary))
elif password_strength == "strong":
    print(generate_strong(chars))
else:
    print("sigh")
