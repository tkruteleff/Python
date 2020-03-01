import random

random_list_a = []
random_list_b = []
compined_list = []

for i in range(0,15):
    n = random.randint(1,30)
    random_list_a.append(n)

for i in range(0,20):
    m = random.randint(1,30)
    random_list_b.append(m)

compined_list = set(random_list_a).intersection(random_list_b)

print(random_list_a)
print(random_list_b)

print(compined_list)
