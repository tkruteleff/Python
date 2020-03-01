divisors = []

def get_integer(help_text):
    return int(input(help_text))

number = get_integer("Give a number: ")

for divisor in range(1, number):
    if(number % divisor == 0):
        divisors.append(divisor)

print(divisors)
