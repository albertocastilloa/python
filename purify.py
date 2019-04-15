"""Function to find not even numbers
V1 
April 10, 2019
"""
def purify(listNumbers):
    newList = []
    for i in listNumbers:
        if i %2 == 0:
            newList.append(i)
    return newList

print(purify([1,2,2]))