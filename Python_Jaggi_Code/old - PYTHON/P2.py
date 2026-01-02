# Create a list with 5 integers and print it
# Find the length of a list without using len().
# Print all elements of a list using a loop.

def size(getList):
    iCount = 0

    for i in getList:
        if(i != None):
            iCount = iCount + 1
    return iCount

def printList(getList):
    print("Elements of list are: ")
    for i in getList:
        if(i != None):
            print(i)

def main():
    myList = []
    iRet = 0

    myList.append(10)
    myList.append(20)
    myList.append(30)
    myList.append(40)
    myList.append(50)

    iRet = size(myList)

    print(iRet)

    printList(myList)

if __name__ == "__main__":
    main()