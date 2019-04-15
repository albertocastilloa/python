"""
Function to sum all given positive numbers
V1
April 10, 2019
"""
def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
    return total

print(digit_sum(87598758947359843753))