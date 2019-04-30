shift_right = 0b0111
shift_left = 0b0111

#Shifting
shift_right = shift_right >> 1
shift_left = shift_left >> 1

print(bin(shift_right))
print(bin(shift_left))

#Bitwise and AND: Only 1 and 1 = 1. Otherwise = 0
print(bin(0b1110 & 0b101))
"""
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
"""
#Bitwise and OR: Only 0 | 0 = 0. Otherwise = 1
print(bin(0b1110 | 0b101))
"""
0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1
"""
#Bitwise and XOR: 0 ^ 1 or 1 ^ 0 = 1. Otherwise = 0
print(bin(0b1110 ^ 0b101))
"""
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
"""
#Bitwise and NOT: Add one to the number and the making it negative
print(~1)
print(~2)
print(~3)
print(~42)
print(~123)