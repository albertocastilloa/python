def count(sequence, item):
    newList = sequence
    counter = 0
    for i in newList:
        if item == i:
            counter +=1
    return counter

print(count([1, 2, 1, 1], 2))