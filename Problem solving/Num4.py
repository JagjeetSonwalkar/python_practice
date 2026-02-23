# Sum of Prime Numbers in a Range
# Count Number of Even and Odd Numbers in Range
# Print All Armstrong Numbers in Range

import math

def sumPrimeNum(getStart, getEnd):
    iSum = 0
    for i in range(getStart, getEnd+1):
        if(math.factorial(i-1) % i) == i-1:
            iSum = iSum + i
    return iSum

def countEvenOddNum(getStart, getEnd):
    iCountEven, iCountOdd = 0, 0
    for i in range(getStart, getEnd+1):
        if i % 2 ==0 :
            iCountEven += 1
        else:
            iCountOdd += 1
    return iCountEven, iCountOdd

def isArmstrong(getNum):
    temp = int(getNum)
    strValue = str(getNum)
    lenght = len(strValue)

    iSum = 0

    getDigit = 0
    while(getNum != 0):
        getDigit = int(getNum % 10)
        iSum += getDigit**lenght
        getNum = getNum // 10

    return iSum == temp

def allArmstrong(getStart, getEnd):
    for i in range(getStart, getEnd+1):
        if isArmstrong(i):
            print(i,end=", ")
    print()

def main():
    Ret = 0
    RetEven, RetOdd = 0, 0

    Ret = sumPrimeNum(10,20)
    print(f"Sum of prime Numbers is {Ret}")

    RetEven, RetOdd = countEvenOddNum(3, 9)
    print(f"count of even number is: {RetEven} & count of odd number is: {RetOdd}")

    allArmstrong(150, 500)

if __name__ == "__main__":
    main()