# Find Maximum and Minimum in List
# Input 1 → [3,1,4,2] → Output 1 → Max:4, Min:1
# Input 2 → [10,50,20] → Output 2 → Max:50, Min:10

# Sum of All Elements in List
# Input 1 → [1,2,3] → Output 1 → 6
# Input 2 → [10,20,30] → Output 2 → 60

# Reverse a List
# Input 1 → [1,2,3] → Output 1 → [3,2,1]
# Input 2 → ['a','b'] → Output 2 → ['b','a']

# Sort List in Ascending Order
# Input 1 → [3,1,2] → Output 1 → [1,2,3]
# Input 2 → [50,10,20] → Output 2 → [10,20,50]

# Sort List in Descending Order
# Input 1 → [3,1,2] → Output 1 → [3,2,1]
# Input 2 → [50,10,20] → Output 2 → [50,20,10]

def maxmin(getList):
    max = getList[0]
    min = getList[0]
    for i in getList:
        if i > max:
            max = i
        elif i < min:
            min = i
    return max, min

def sumAllElement(getList):
    iSum = 0
    for i in getList:
        iSum += i
    return iSum

def reveseList(getList):
    newList = []
    value = 0
    for i in range(len(getList)-1,-1,-1):
        value = getList[i]
        newList.append(value)
    return newList
        
def sortAsc(getList):
    temp = 0
    for i in range(len(getList)-1):
        for j in range(len(getList)-i-1):
            if getList[j] > getList[j+1]:
                temp = getList[j]
                getList[j] = getList[j+1]
                getList[j+1] = temp
    return getList

def sortDesc(getList):
    temp = 0
    for i in range(len(getList)-1):
        for j in range(len(getList)-i-1):
            if getList[j] < getList[j+1]:
                temp = getList[j]
                getList[j] = getList[j+1]
                getList[j+1] = temp
    return getList    

def main():
    numList = [1, 0, 9, 50, 3, 2, 5, 25, 10, 2003]
    print("Original list: ",numList)

    Ret, Ret2 = 0, 0

    Ret, Ret2 = maxmin(numList)
    print(f"Max element from the list is {Ret} & Min is {Ret2}")

    Ret = sumAllElement(numList)
    print("Sum of all elements in list is: ",Ret)

    Ret = reveseList(numList)
    print("Reverse list: ",Ret)

    Ret = sortAsc(numList)
    print("Sort List in Ascending Order:",Ret)

    Ret = sortDesc(numList)
    print("Sort List in Descending Order:",Ret)

if __name__ == "__main__":
    main()