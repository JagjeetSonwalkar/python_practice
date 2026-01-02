# Count Occurrences of an Element
# Input 1 → [1,2,2,3], count 2 → Output 1 → 2

# Find Index of First Occurrence of Element
# Input 2 → ['x','y','x'], index of 'x' → Output 2 → 0

# Remove All Occurrences of an Element
# Input 1 → [1,2,2,3], remove 2 → Output 1 → [1,3]

# Flatten a List of Lists
# Input 1 → [[1,2],[3,4]] → Output 1 → [1,2,3,4]

# Merge Two Lists Element-wise
# Input 1 → [1,2],[3,4] → Output 1 → [1,3,2,4]

def occurrences(getList, getElement):
    iCount = 0
    for i in getList:
        if i == getElement:
            iCount += 1
    return iCount

# Find Index of First Occurrence of Element
def getIndex(getList, getElement):
    index = 0
    for i in getList:
        if i == getElement:
            return index
        index += 1

def removeAllOccurrences(getList, getElement):
    newList = []
    for i in getList:
        if i != getElement:
            newList.append(i)
    return newList

def flattenList(getList):
    newList = []
    value = 0
    for sublist in getList:
        for i in sublist:
            newList.append(i)
    return newList

def mergeListElementWise(getList1, getList2):
    if len(getList1) != len(getList2):
        return False
    newList = []
    value = 0
    for i in range(len(getList1)):
        value = getList1[i]
        newList.append(value)
        value = getList2[i]
        newList.append(value)
    return newList


def main():
    numList = [1,2,2,3]
    numList1 = ['x','y','x']
    numList2 = [[1,2],[3,4]]
    numList3 = [3,4,3,4]
    element = 0

    element = int(input("Enter the element to count the occurrences: "))
    Ret = occurrences(numList, element)
    print(f"Occurrences of an Element '{element}' is '{Ret}'")

    element = input("Enter the element to Find Index of First Occurrence of Element: ")
    Ret = getIndex(numList1, element)
    print(f"Index of First Occurrence of Element '{element}' is:'{Ret}'")

    element = int(input("Enter the element to Remove All Occurrences of an Element: "))
    Ret = removeAllOccurrences(numList, element)
    print(f"orignal list '{numList}' & Remove All Occurrences of an Element '{element}' is: {Ret}")

    Ret = flattenList(numList2)
    print("Orignal list ",numList2,", New list:",Ret)

    Ret = mergeListElementWise(numList, numList3)
    print(f"List1 = {numList} & List2 = {numList3}, Merge Two Lists Element-wise {Ret}")

if __name__ == "__main__":
    main()