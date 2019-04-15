"""Function to get prime numbers
V1 
April 10, 2019
"""

def is_prime(x):
    if x < 2:
        return False
    for n in range(2,x):
        print(x,"%",n,"=",(x % n))
        if x % n == 0:
            return False
    return True

print(is_prime(11))