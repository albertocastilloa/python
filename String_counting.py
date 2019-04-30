"""
EXERCISE 1:
Finding letters into a variable, count it and return the final result.
"""
#FIND LETTERS INTO A VARIABLE AND COUNT IT
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
    counter = 0
    for i in letters:
        if i in word:
            counter += 1
    return counter
#print(unique_english_letters("mississippi"))


"""
EXERCISE 2:
Write a function named count_char_x that takes a string named word 
and a single character named x as parameters. The function should return 
the number of times x appears in word.
"""
def count_char_x(word, s):
    counter = 0
    for i in word:
        if s in i:
            counter += 1
    return counter
#print(count_char_x("mississippi", "s"))

"""
EXERCISE 3:
Write a function named count_multi_char_x that takes a string named word 
and a string named x. This function should do the same thing as 
the count_char_x function you just wrote - it should return 
the number of times x appears in word. However, this time, make sure 
your function works when x is multiple characters long.

For example, count_multi_char_x("Mississippi", "iss") should return 2
"""
def count_multi_char_x(word, s):
    counter = word.count(s)
    return counter
#print(count_multi_char_x("mississippi", "iss"))


"""
EXERCISE 4:
Write a function named substring_between_letters that takes a string named word,
 a single character named start, and another character named end. 
 This function should return the substring between the first occurrence of 
 start and end in word. If start or end are not in word, the function should 
 return word.

For example:
substring_between_letters("apple", "p", "e") should return "pl".
"""

def substring_between_letters(word, start, end):
    if word.find(start) != -1 and word.find(end) != -1:
        return start + word[word.find(end)-1]
        #return word[word.find(start):word.find(end)]
    else:
        return word

#print(substring_between_letters("apple", "p", "e"))

"""
EXERCISE 5:
Create a function called x_length_words that takes a string named sentence and 
an integer named x as parameters. This function should return True if every 
word in sentence has a length greater than or equal to x.
"""

def x_length_words(sentence, x):
    newLine = sentence.split(" ")
    for i in newLine:
        if len(i) < int(x):
            return False
            break
    return True

#print(x_length_words("he like apples", 2))

"""
EXERCISE 6
Write a function called check_for_name that takes two strings as parameters 
named sentence and name. The function should return True if name 
appears in sentence in all lowercase letters, all uppercase letters, or with 
any mix of uppercase and lowercase letters. The function should 
return False otherwise.

For example, the following three calls should all return True:
"""
def check_for_name(sentence, name):
    sentence_lower = sentence.lower()
    name_lower = name.lower()
    if sentence_lower.find(name_lower) != -1:
        return True
    else:
        return False

#print(check_for_name("My name is Jamie", "Jamie"))
#print(check_for_name("My name is jamie", "Jamie"))
#print(check_for_name("My name is Samantha", "Jamie"))

"""
EXERCISE  7:
Create a function named every_other_letter that takes a string named 
word as a parameter. The function should return a string containing every 
other letter in word.
"""

def every_other_letter(word):
    newWord = ''
    i = 0
    while i < len(word):
        newWord = newWord + word[i]
        i += 2
    return newWord

#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print 

"""
EXERCISE  8:
Write a function named reverse_string that has a string named word 
as a parameter. The function should return word in reverse.
"""
def reverse_string(word):
    return word[::-1]

#print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print

"""
EXERCISE  9:
A Spoonerism is an error in speech when the first syllables of two words 
are switched. For example, a Spoonerism is made when someone says 
“Belly Jeans” instead of “Jelly Beans”.

Write a function called make_spoonerism that takes two strings as parameters 
named word1 and word2. Finding the first syllable of a word is a difficult 
task, so for our function, we’re going to switch the first letters of each 
word. Return the two new words as a single string separated by a space.
"""

def make_spoonerism(word1, word2):
    first_letter = word1[0]
    second_letter = word2[0]
    newWord1 = second_letter + word1[1:]
    newWord2 = first_letter + word2[1:]

    return newWord1 + " " + newWord2

#print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
# should print b a

"""
EXERCISE  10:
Create a function named add_exclamation that has one parameter named word. 
This function should add exclamation points to the end of word until word 
is 20 characters long. If word is already at least 20 characters long, 
just return word.
"""
def add_exclamation(word):
    exclamation = ''
    if len(word) >= 20:
        return word
    else:
        for i in range(0,20 - len(word)):
            exclamation += "!"
    return word + exclamation

print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn