# Factorial of a Number using Loop
# Print Multiplication Table of a Number
# Sum of Digits of a Number using Loop
# Print Reverse Numbers from N to 1
# Check if Number is Palindrome using Loop

def findFactorial(getNum):
    fact = 1

    if(getNum < 0):
        return "ERROR - pls, enter +ve Number"
    elif(getNum == 0):
        return fact
    
    for i in range(1, getNum+1):
        fact *= i
        print(i,end=", ")
    print()
    return fact

def printTables(getNum):
    if(getNum < 0):
        return "ERROR - pls, enter +ve Number"
    
    for i in range(1,11,1):
        print(getNum*i,end=" ")
    print()

def countDigit(getNum):
    if(getNum < 0):
        getNum = -getNum
    
    iCount = 0

    while(getNum != 0):
        iDigit = int(getNum % 10)
        iCount += 1
        getNum = int(getNum / 10)
    return iCount

def sumDigit(getNum):
    if(getNum < 0):
        getNum = -getNum
    
    iSum = 0
    while(getNum != 0):
        iDigit = int(getNum % 10)
        print(iDigit)
        iSum += iDigit
        getNum = int(getNum / 10)
    return iSum

def reverseNum(getNum):
    if(getNum < 0):
        getNum = -getNum
    
    while(getNum != 0):
        iDigit = int(getNum % 10)
        print(iDigit,end="")
        getNum = int(getNum / 10)
    print()

def isPalindrome(getNum):
    orignalNum = getNum
    if(getNum < 0):
        getNum = -getNum

    revNum = ""
    
    while(getNum != 0):
        iDigit = int(getNum % 10)
        revNum = revNum + str(iDigit)
        getNum = int(getNum / 10)

    if(orignalNum == int(revNum)):
        return True

def main():
    num, iRet = 0, 0
    bRet = False

    num = int(input("Enter the num to print factorial: "))
    iRet = findFactorial(num)
    print("Factroial of",num,"is:",iRet)

    num = int(input("Enter the number to print table: "))
    printTables(num)

    num = int(input("Enter the number to check total digit(if num is -ve then it will get converted into +ve: "))
    iRet = countDigit(num)
    print("Total digit in ",num,"is:",iRet)

    num = int(input("Enter the number to sum total digit(if num is -ve then it will get converted into +ve: "))
    iRet = sumDigit(num)
    print("Sum of Total digit is ",num,"is:",iRet)
    
    num = int(input("Enter the number to reverse(if num is -ve then it will get converted into +ve): "))
    reverseNum(num)
    
    num = int(input("Check number is Palindrome or Not: "))
    bRet = isPalindrome(num)
    if(bRet is True):
        print(num,": is palindrome Number")
    else:
        print(num,": is palindrome NOT Number !")

if __name__ == "__main__":
    main()