# Print Sum of First N Even Numbers
# Print Sum of First N Odd Numbers
# Print Fibonacci Series up to N Terms
# Find Prime Numbers up to N

import math

def sumFirstEvenNum(getRange):
    if(getRange < 0):
        return "ERROR - pls, enter +ve Number"
    
    iSum, num, iCount = 0, 1, 0
    while(iCount != getRange):
        if(num % 2 == 0):
            iSum = iSum + num
            iCount = iCount + 1
        num += 1
    return iSum

def sumFirstOddNum(getRange):
    if(getRange < 0):
        return "ERROR - pls, enter +ve Number"
    
    iSum, num, iCount = 0, 1, 0
    while(iCount != getRange):
        if(num % 2 != 0):
            iSum = iSum + num
            iCount = iCount + 1
        num += 1
    return iSum

def printFibnacci(getRange):
    if(getRange < 0):
        return "ERROR - pls, enter +ve Number"
    elif(getRange == 0):
        return 0
    
    num = 1
    iCount = 2
    fNum = 0
    sNum = 1
    tNum = 0
    print(fNum,sNum,end=" ")
    while(iCount != getRange):
        tNum = fNum + sNum
        print(tNum,end=" ")
        fNum = sNum
        sNum = tNum
        tNum = 0
        num += 1
        iCount = iCount + 1
    print()

def printPrimeNum(getNum):
    if getNum < 0:
        return "ERROR - pls, enter +ve"
    
    for i in range(2, getNum+1):
        if math.factorial(i-1) % i == i - 1:
            print(i,end=", ")
    print()
       

def main():
    num, iRet = 0, 0

    num = int(input("Enter the number to sum the first n even number: "))
    iRet = sumFirstEvenNum(num)
    print("Sum of first",num,"Even Numbers is:",iRet)

    num = int(input("Enter the number to sum the first n odd number: "))
    iRet = sumFirstOddNum(num)
    print("Sum of first",num,"odd Numbers is:",iRet)

    num = int(input("Enter the number to print fibonacci Num: "))
    printFibnacci(num)

    num = int(input("Enter the num to display prime Number: "))
    printPrimeNum(num)

if __name__ == "__main__":
    main()