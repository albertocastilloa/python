"""Function to remove duplicate numbers/string from a given list
V1 
April 10, 2019
"""
def remove_duplicates(numList):
  newList = []
  for i in numList:
      if i not in newList:
        newList.append(i)
  return newList

print(remove_duplicates([4, 5, 5, 4]))