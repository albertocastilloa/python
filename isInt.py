"""Function to identify a number as integer
V1 
April 10, 2019
"""
def is_int(x):
    absoluteCount = abs(x)
    typeCount =type(x)
    roundCount = round(absoluteCount)
    if typeCount and absoluteCount - roundCount == 0:
        return True
    else:
        return False

print(is_int(-54.56))