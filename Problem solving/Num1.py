# Print Numbers from 1 to N
# Print Even Numbers up to N
# Print Odd Numbers up to N
# Sum of First N Natural Numbers

def printNum(getFirstNum, getLastNum):
    for i in range(getFirstNum,getLastNum+1):
        print(i,end=", ")
    print()

def printEvenNum(getFirstNum, getLastNum):
    for i in range(getFirstNum, getLastNum+1):
        if(i % 2 == 0):
            print(i,end=", ")
    print()

def printOddNum(getFirstNum, getLastNum):
    for i in range(getFirstNum, getLastNum+1):
        if(i % 2 != 0):
            print(i,end=", ")
    print()

def sumNum(getFirstNum, getLastNum):
    iSum = 0
    for i in range(getFirstNum, getLastNum+1):
        iSum = iSum + i
    return iSum

def main():
    firstNum, lastNum, iRet = 0, 0, 0

    firstNum = int(input("Enter the Number from the it should start: "))
    lastNum = int(input("Enter the number where it should be stop: "))
    printNum(firstNum, lastNum)

    firstNum = int(input("Enter the Number from the it should start printing even num: "))
    lastNum = int(input("Enter the number where it should be stop: "))
    printEvenNum(firstNum, lastNum)

    firstNum = int(input("Enter the Number from the it should start printing Odd num: "))
    lastNum = int(input("Enter the number where it should be stop: "))
    printOddNum(firstNum, lastNum)

    firstNum = int(input("Enter the Number from the it should start sum first n num: "))
    lastNum = int(input("Enter the number where it should be stop: "))
    iRet = sumNum(firstNum, lastNum)
    print("The sum of first n natural number of",firstNum,"to",lastNum,"is:",iRet)

if __name__ == "__main__":
    main()