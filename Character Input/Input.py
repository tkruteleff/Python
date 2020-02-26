import datetime

name = input("Give me your name: ")
age = int(input("Enter your age: "))
copies = int(input("Enter number of copies "))

ageDifference = 100 - age
currentYear = datetime.datetime.now()

whenHundred = currentYear.year + ageDifference

i = 0
while i < copies:
    print("Your name is " + name + " and you will one hundred years old in", whenHundred)
    i += 1
