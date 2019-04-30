def fib(input):
 if (input <=1):
   return(str(input))
 else:
   first = 0
   second = 1
   count = 0
   for count in range(input):
     result = first + second
     print(first)
     first = second
     second = result
     count = count+1

fib(7)