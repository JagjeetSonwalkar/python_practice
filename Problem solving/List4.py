# Remove Duplicates from List
# Input 1 → [1,2,2,3] → Output 1 → [1,2,3]
# Input 2 → ['a','b','a'] → Output 2 → ['a','b']

# Find Common Elements Between Two Lists
# Input 1 → [1,2,3],[2,3,4] → Output 1 → [2,3]
# Input 2 → ['a','b'],['b','c'] → Output 2 → ['b']

# Find Elements Present in One List but Not Another
# Input 1 → [1,2,3],[2,3,4] → Output 1 → [1]
# Input 2 → ['a','b'],['b','c'] → Output 2 → ['a']

# Rotate List to Right by N Positions
# Input 1 → [1,2,3,4],2 → Output 1 → [3,4,1,2]
# Input 2 → [a,b,c],1 → Output 2 → [c,a,b]

# Rotate List to Left by N Positions
# Input 1 → [1,2,3,4],2 → Output 1 → [3,4,1,2]
# Input 2 → [a,b,c],1 → Output 2 → [b,c,a]

# Remove Duplicates from List
def removeDuplicates(getList):
    newSet = set(getList)
    getList = list(newSet)
    return getList

# Find Common Elements Between Two Lists
def commonElement(getList):
    commonList = []
    list1, list2 = getList[0], getList[1]
    value = 0
    for i in range(len(list1)):
        if list1[i] in list2:
            value = list1[i]
            commonList.append(value)
    return commonList

# Find Elements Present in One List but Not Another
def uniqueElement(getList):
    uniqueList, list1, list2, value = [], [], [], 0
    list1 = getList[0]
    list2 = getList[1]

    for i in list1:
        if i in list2:
            pass
        else:
            uniqueList.append(i)
    return uniqueList

def rotateListR(getList, getPosition):
    newList = []
    newList = getList[getPosition:] + getList[:-getPosition]
    print(newList)

def rotateListL(getList, getPosition):
    newList = []
    newList = getList[getPosition:] + getList[:getPosition]
    print(newList)

def main():
    numList = [1,2,2,3]

    Ret, iPos = None, 0

    # Ret = removeDuplicates(numList)
    # print(f"Orignal list {numList} and After Remove Duplicates from List: {Ret} ")

    # numList = [1,2,3],[2,3,4]
    # Ret = commonElement(numList)
    # print(f"{numList} Common element from the list is: {Ret}")

    # Ret = uniqueElement(numList)
    # print(f"{numList} unique element from the list is: {Ret}")

    numList = [1,2,3,4]
    iPos = 2
    rotateListR(numList, iPos)

    rotateListL(numList, iPos)

if __name__ == "__main__":
    main()