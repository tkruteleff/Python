number = int(input("Give a number "))
check = int(input("Give a number to divide by "))

if ((number % 2) == 0) & ((number % 4) != 0):
    print("Number is even")
elif (number % 4) == 0:
    print("Number is even and multiple of 4")
else:
    print("Number is not even")

if (number % check) == 0:
    print(number, "divides evenly")
else:
    print(number, "does not divide evenly")
