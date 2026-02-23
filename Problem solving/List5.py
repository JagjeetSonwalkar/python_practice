# Find Second Largest Element in List
# Input 1 → [3,1,4,2] → Output 1 → 3
# Input 2 → [50,10,20] → Output 2 → 20

# Find Second Smallest Element in List
# Input 1 → [3,1,4,2] → Output 1 → 2
# Input 2 → [50,10,20] → Output 2 → 20

# Split List into Chunks of Size N
# Input 1 → [1,2,3,4,5],2 → Output 1 → [[1,2],[3,4],[5]]
# Input 2 → [a,b,c,d],3 → Output 2 → [[a,b,c],[d]]

# Replace All Occurrences of an Element
# Input 1 → [1,2,2,3], replace 2 with 5 → Output 1 → [1,5,5,3]
# Input 2 → ['a','b','a'], replace 'a' with 'x' → Output 2 → ['x','b','x']

# Find Sum of Elements at Even Indices
# Input 1 → [1,2,3,4] → Output 1 → 1+3=4
# Input 2 → [10,20,30,40] → Output 2 → 10+30=40

def secondMax(getList):
    max1, max2 = getList[0], getList[0]
    for i in getList:
        if i > max1:
            max2 = max1
            max1 = i
        if i > max2 and i != max1:
            max2 = i
    print(max2)

def secondMin(getList):
    min1, min2 = getList[0], getList[0]
    for i in getList:
        if i < min1:
            min2 = min1
            min1 = i
        if i < min2 and i != min1:
            min2 = i
    print(min1, min2)

def splitList(getList, getSize):
    newList = []
    subList = []
    for i in getList:
        if len(subList) == getSize:
            newList.append(subList)
            subList = []
        subList.append(i)
    if subList != len(subList):
        newList.append(subList)

    print(newList)

def replacelistoccurence(getList, replaceElement, replaceWith):
    newList = []
    for i in getList:
        if i == replaceElement:
            i = replaceWith
        newList.append(i)
    print(newList)

def sumofevenindiceselement(getList):
    iSum = 0
    index = 0
    for i in getList:
        if index % 2 == 0:
            iSum += i
        index += 1
    print(iSum)
        
def main():
    myList = [3,20,1,4,6,2,5,15]

    secondMax(myList)
    secondMin(myList)
    splitList(myList, 4)
    replacelistoccurence(myList, 20, 22)

    myList = [1,2,3,4]
    sumofevenindiceselement(myList)

    myList = [10,20,30,40]
    sumofevenindiceselement(myList)
    


if __name__ == "__main__":
    main()