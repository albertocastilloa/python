#12 == 0b1100
def check_bit4(number):
    bitNumber = number
    mask = 0b1000
    desire = bitNumber & mask
    if desire > 0:
        return "on"
    else:
        return "off"

print(check_bit4(0b1100))