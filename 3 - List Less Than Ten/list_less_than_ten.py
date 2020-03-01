a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

user_given_value = int(input("Give a number "))

for element in a:
    if element < user_given_value:
        new_list.append(element)
print("New list",new_list)
