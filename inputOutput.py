"""
my_list = [i ** 2 for i in range(1,16)]

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")
    
f.close()
"""

"""
other_comprehensive_list = [x for x in range(1,101) if (x % 2 == 0)]

my_file = open("outputWR.txt", "w")

for items in other_comprehensive_list:
    my_file.write(str(items) + "\n")

my_file.close()

my_file = open("outputWR.txt", "r")
print(my_file.read())
my_file.close()

my_file = open("outputWR.txt", "r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readlines())
my_file.close()
"""

with open("automaticllyClosed.txt", "w") as textfile:
    textfile.write("Success")

if not textfile.closed:
    textfile.close()
    print("File has been closed")
else:
    print("FILE CLOSED")
    