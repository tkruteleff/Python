list_A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]

def removeSetsList(list_A):
    list_B = set(list_A)
    return list_B


def removeDublicatesList(list_A):
    y = []
    for i in list_A:
        if i not in y:
            y.append(i)
    return y

print(removeSetsList(list_A))
print(removeDublicatesList(list_A))
