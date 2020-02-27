import random

aList = random.sample(range(1,20), 10)
bList = random.sample(range(1,20), 10)
c = set(a for a in aList if a in bList)

print(c)
