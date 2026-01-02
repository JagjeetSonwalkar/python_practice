# Find the index of all occurrences of a given element.

def findIndexOccrences(getList, getValue):
    indexListX = []
    iIndexValue = 0

    for i in getList:
        if(i == getValue):
            indexListX.append(iIndexValue)
        iIndexValue = iIndexValue + 1
    
    return indexListX


def main():
    value = 0
    Ret = 0

    myList = [10, 20, 20, 30, 10, 20, 50, 60, 50]

    value = int(input("Enter the value to check occureences: "))

    Ret = findIndexOccrences(myList, value)

    print("The index of all occurrences: ",Ret)

if __name__ == "__main__":
    main()