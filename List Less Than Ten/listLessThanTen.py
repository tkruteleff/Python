a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

userGivenValue = int(input("Give a number "))

for element in a:
    if element < userGivenValue:
        newList.append(element)
print("New list",newList)
