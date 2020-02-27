import random

randomlistA = []
randomListB = []
compinedList = []

for i in range(0,15):
    n = random.randint(1,30)
    randomlistA.append(n)

for i in range(0,20):
    m = random.randint(1,30)
    randomListB.append(m)

compinedList = set(randomlistA).intersection(randomListB)

print(randomlistA)
print(randomListB)

print(compinedList)
