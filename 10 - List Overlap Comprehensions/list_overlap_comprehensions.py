import random

a_list = random.sample(range(1,20), 10)
b_list = random.sample(range(1,20), 10)
c = set(a for a in a_list if a in b_list)

print(c)
