# Sum of Factorials of Numbers in Range
# Find Largest Digit in a Number Using Loop
# Count Number of Times a Digit Appears in Range

import math

def sumFactorialsNum(getStart, getEnd):
    iSum = 0
    for i in range(getStart, getEnd+1):
        iSum += math.factorial(i)
    return iSum

def largestDigit(getNum):
    maxDigit, iDigit = 0, 0

    firstDigit = str(getNum)
    maxDigit = int(firstDigit[0])

    while(getNum != 0):
        iDigit = getNum % 10
        if(iDigit > maxDigit):
            maxDigit = iDigit
        getNum = getNum // 10

    return maxDigit

def minDigit(getNum):
    minDigit, iDigit = 0, 0

    firstDigit = str(getNum)
    minDigit = int(firstDigit[0])

    while(getNum != 0):
        iDigit = getNum % 10
        if minDigit > iDigit:
            minDigit = iDigit
        getNum = getNum // 10

    return minDigit

def countDigitAppears(getStart, getEnd, getDigit):
    myDict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    runIndex = 0
    count = 0

    for i in range(getStart, getEnd+1):
        num = i
        while(num != 0):
            iDigit = num % 10
            myDict[iDigit] += 1
            num = num // 10

    count = myDict[getDigit]

    return count


def main():
    Ret = 0
    iStart, iEnd = 0, 0
    myNum = 0
    iDigit = 0

    iStart, iEnd = 2, 4

    Ret = sumFactorialsNum(iStart, iEnd)
    print(f"Sum of Factorials of Numbers in Range {iStart} to {iEnd} is: {Ret}")

    myNum = 571
    Ret = largestDigit(myNum)
    print(f"Max digit of number {myNum} is: {Ret}")

    myNum = 7190
    Ret = minDigit(myNum)
    print(f"Min digit of number {myNum} is: {Ret}")

    iStart, iEnd, iDigit = 1, 20, 1
    Ret = countDigitAppears(iStart, iEnd, iDigit)
    print(f"Count Number of Times a Digit: {iDigit}, Appears in Range {iStart} to {iEnd} is: {Ret}")
if __name__ == "__main__":
    main()