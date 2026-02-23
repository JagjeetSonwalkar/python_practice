# Find common elements in two lists.

def contain(getList, value):
    for i in getList:
        if(i == value):
            return True
    return False

def commonElements(getList1, getList2):
    commonElement = []

    for i in range(len(getList1)):
        first = getList1[i]

        for j in range(len(getList2)):
            if(first == getList2[j]):
                if(contain(commonElement,first) == False):
                    commonElement.append(first)
        
    return commonElement

def main():

    myList1 = [1, 4, 7, 9, 2, 3, 5, 6, 8, 0]
    myList2 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]

    print("first list: ",myList1)
    print("second list: ",myList2)

    Ret = commonElements(myList1, myList2)

    print("Common elements from the lists are: ",Ret)


if __name__ == "__main__":
    main()