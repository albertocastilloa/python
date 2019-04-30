
#List comprehension
evenNumbers = [x for x in range(1,101) if (x % 2 == 0)]
print("Even Numbers: ", evenNumbers)
#Lambda
notEven5 = list(filter(lambda y: y%5==0,evenNumbers))
print(notEven5)

print(evenNumbers[0])

a ={
    "A": "Que la shit"
} 
print(notEven5.index("10"))