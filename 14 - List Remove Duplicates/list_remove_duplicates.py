list_a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]

def remove_sets_list(list_a):
    list_b = set(list_a)
    return list_b


def remove_dublicates_list(list_a):
    y = []
    for i in list_a:
        if i not in y:
            y.append(i)
    return y

print(remove_sets_list(list_a))
print(remove_dublicates_list(list_a))
