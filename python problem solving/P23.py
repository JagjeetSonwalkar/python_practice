# Find the sum of digits of all numbers in a list.
# return a list of sum of digits of each element.

def sumAllDigits(getList):
    iSum = 0
    for value in getList:
        while(value != 0):
            idigit = int(value % 10)
            iSum = iSum + idigit
            value = int(value / 10)
    return iSum

def sumDigit(getList):
    sumDigitList = []
    iSum = 0
    for value in getList:
        while(value != 0):
            idigit = int(value%10)
            iSum = iSum + idigit
            value = int(value / 10)
        sumDigitList.append(iSum)
        iSum = 0
    
    return sumDigitList

def main():
    Ret = 0
    myList = [10, 100, 25, 2510, 2003, 25102003]

    print("Orignal list: ",myList)

    Ret = sumAllDigits(myList)
    print("Sum of all digits of list is: ",Ret)

    Ret = sumDigit(myList)
    print("Sum of digit of every element is: ",Ret)



if __name__ == "__main__":
    main()