"""Function to reverse a given word
V1 
April
"""
def reverse(text):
    newWord = ""
    counter = len(text)-1
    for n in text:
        newWord += text[counter]
        counter -= 1
    return newWord

print (reverse("Python albertocastillo$"))