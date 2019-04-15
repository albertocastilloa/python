"""
Function to use asterisk to censor a word
V1
April 11, 2019
"""

def censor(text, word):
    textList = text.split()
    newWord = ""
    for i in range(0, len(textList)):
        if textList[i] == word:
            textList[i] = ("*" * len(textList[i]))
            newWord = " ".join(textList)
    return newWord

print(censor("Bro, this is a great night, hey you right, hey you know", "hey"))