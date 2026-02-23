# Split a list into two halves.

def split(getList):
    newList1 = []
    newList2 = []

    index = int(len(getList)/2)

    for i in range(0, index, 1):
        newList1.append(getList[i])
    
    for i in range(index, len(getList), 1):
        newList2.append(getList[i])

    print(newList1)
    print(newList2)

    return newList1, newList2

def main():

    myList1 = [1, 4, 7, 9, 2, 3, 5, 6, 8, 0]

    print(myList1)

    Ret = split(myList1)

    print(Ret)


if __name__ == "__main__":
    main()