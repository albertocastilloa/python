"""Function to get product from a given list
V1 
April 10, 2019
"""
def product(prodList):
    total = 1
    for i in prodList:
        total *= i
    return total

print(product([6, 6, 6, 6, 6]))