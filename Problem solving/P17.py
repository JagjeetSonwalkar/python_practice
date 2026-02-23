# Find elements present in one list but not in another

def contain(getList, value):
    for i in getList:
        if(i == value):
            return True

def differentElements(getList1, getList2):
    differentElement = []

    differentElement = list(set(getList1) - set(getList2))

    return differentElement

def main():

    myList1 = [4, 7, 9, 2, 3, 5, 6, 8, 0]
    myList2 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]

    print("first list: ",myList1)
    print("second list: ",myList2)

    Ret = differentElements(myList1, myList2)

    print("elements which are not present in list2: ",Ret)


if __name__ == "__main__":
    main()