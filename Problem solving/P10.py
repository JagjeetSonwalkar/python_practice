#	Remove duplicates from a list

def check(getValue, getList):
    for i in getList:
        if(getValue == i):
            return True
    return False

def removeDuplicates(getList):
    newList = []
    Ret = 0

    for value in getList:
        Ret = check(value, newList)
        if(Ret == False):
            newList.append(value)

    return newList

def main():

    myList = [1, 2, 3, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9]

    print(myList)

    newList = removeDuplicates(myList)
    
    print(newList)

if __name__ == "__main__":
    main()