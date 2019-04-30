
"""
Changin value of a bit using mask and NOT operator. Third bit must turn on
"""
a = 0b10111011 #187
bitmask = 0b101
desire = a | bitmask
print(bin(desire))

"""
Changin value of a bit using mask and XOR operator. Flip all bits on
"""
print("Using XOR to flip all bits")
x = 0b11101110
y = 0b11111111
desire2 = x ^ y
print(bin(x))
print(bin(desire2))

print("SLIP AND SLIDE")
bitMask2 = (0b1 << 9)
print(bin(bitMask2))