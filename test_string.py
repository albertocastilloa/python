"""
Do not use this file. Just for learning purpose
April 11, 2019
"""
x = ["chat","dog","pet","cat","dog"]
y = [1,2,2,4,6,2,7,7,2]

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}



def scrabble_score(word):
    points = 0
    for i in word.lower():
        print(i)
        if i in score:
            points += score[i]
    return points

print(scrabble_score("Hola"))