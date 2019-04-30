import time

def rgbChecker(rgbValue):
    if rgbValue >= 0 and rgbValue <= 255:
        return True
    else:
        return False

def rgb_hex():
    invalid_msg = "Error sending rgb_hex"
    red = int(input("Enter RED value: "))
    if rgbChecker(red) == False:
        print("Error un RED value, please try again:")
        return
    green = int(input("Enter GREEN value: "))
    if rgbChecker(green) == False:
        print("Error un GREEN value, please try again:")
        return
    blue = int(input("Enter BLUE value: "))
    if rgbChecker(blue) == False:
        print("Error un BLUE value, please try again:")
        return
    val = (red << 16) + (green << 8) + blue
    val = hex(val)
    val = val.upper()
    print(val[2::])

def hex_rgb():
    hex_val = input("Enter a hexadecimal value: ")
    if len(hex_val) != 6:
        print("It's not a hexadecimal value")
        return
    else:
        hex_val = int(hex_val, 16)
    two_hex_digits = 2**8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits
    print("Red: %s Green: %s Blue: %s" % (red, green, blue))

def convert():
    start = True
    option = ""
    while start:
        option = str(input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:"))
        if option == "1":
            print("RGB to HEX converter actived...")
            time.sleep(1)
            rgb_hex()
        elif option == "2":
            print("HEX to RGB converter actived...")
            time.sleep(1)
            hex_rgb()
        elif option == "X" or option == "x":
            print("Good bye")
            start = False
        else:
            continue


convert()