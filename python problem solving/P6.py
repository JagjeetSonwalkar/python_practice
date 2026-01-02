# Count the occurrences of an element in a list
# Convert a string into a list of characters
# Copy a list without using copy() method.

def copyList(getList):
    newList = []

    for i in getList:
        newList.append(i)
    return newList

def toString(getString):
    newList = []

    for i in getString:
        if i == " ":
            pass
        else:
            newList.append(i)

    return newList

def countOccuurences(getList, getValue):
    iCount = 0

    for i in getList:
        if(i == getValue):
            iCount = iCount + 1
    return iCount

def main():
    getRetrun = 0

    myList = [10, 2 ,9,7, 2, 1, 10, 4, 100, 5, 1, 7, 7]

    getRetrun = countOccuurences(myList, 0)
    print("Count the occurrences of an element in a list is: ",getRetrun)

    myString = "This is String"

    myNewList = []

    myNewList = toString(myString)
    print("String is: ",myString)
    print("String to list is: ")
    print(myNewList)

    copylistX = []
    copylistX = copyList(myList)
    print("Original: ",myList)
    print("Copy list: ",copylistX)

if __name__ == "__main__":
    main()