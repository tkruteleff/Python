number = int(input("Give a number "))

divisors = []

for divisor in range(1, number):
    if(number % divisor == 0):
        divisors.append(divisor)

print(divisors)
