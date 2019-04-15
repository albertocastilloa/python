"""
Function to remove Vowels from a string
V1
April 10, 2019
"""

def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result
print(anti_vowel("hello book"))