def gen_fibonacci(number_count):
    count = int(input(number_count))
    num1 = 0
    num2 = 1
    sequence = []

    for x in range(count + 1):
        num1, num2 = num2, num1 + num2
        sequence.append(num1)

    print(sequence)

fibonacci_length = gen_fibonacci("Give a number: ")
