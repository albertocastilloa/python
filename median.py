"""Function to get median from a given number
V1 
April 14, 2019
"""
def median(numList):
    print(sorted(numList))
    if len(numList) %2 == 0:
        numListSorted = sorted(numList)
        middleNumber = int(len(numListSorted)/2)
        medianNumber = (numListSorted[(middleNumber - 1)] + numListSorted[(middleNumber)]) / (2.0)
        return medianNumber
    else:
        numListSorted = sorted(numList)
        medianNumber = numListSorted[int(len(numListSorted)/2)]
        return medianNumber


print(median([2, 103]))