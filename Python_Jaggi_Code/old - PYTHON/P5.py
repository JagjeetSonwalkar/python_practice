# Sort a list in ascending order
# Sort a list in descending order
# Find the maximum element in a list.
# Find the minimum element in a list
# Calculate the sum of elements in a list
# Check if an element exists in a list.

def check(getList, getValue):
    for i in getList:
        if(i == getValue):
            return True
    return False

def findMax(getList):
    maxElement = getList[0]

    for i in getList:
        if(maxElement < i):
            maxElement = i
    
    return maxElement

def findMin(getList):
    minElement = getList[0]

    for i in getList:
        if(minElement > i):
            minElement = i
    
    return minElement

def sumList(getList):
    iSum = 0

    for i in getList:
        iSum = iSum + i
    return iSum

def main():
    iRet = 0

    myList = [10, 2 ,9, 4, 100, 5, 1, 7]
    
    iRet = findMax(myList) # maximum element
    print("Max element from the list is: ",iRet)

    iRet = findMin(myList) # minimum element
    print("Min element from list: ",iRet)

    iRet = sumList(myList) # sum of elements in a list
    print("Sum of list is: ",iRet)

    iRet = check(myList, 5)
    if(iRet == True):
        print("Element is present in the list")
    else:
        print("Element is not present in the list")

    myList.sort() # ascending
    print(myList)

    myList.sort(reverse=True) # descending
    print(myList)

    



if __name__ == "__main__":
    main()