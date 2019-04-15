"""Function to get factorial of a given number
V1 
April 10, 2019
"""

def factorial(x):
  if x == 0 or x == 1:
    return x
  else:
      i = 1
      while x > 0:
        i *= x
        x -= 1
        print(x)
  return i

print(factorial(4))