# Find All Pairs with Given Sum
# Input 1 → [1,2,3,4],5 → Output 1 → [(1,4),(2,3)]
# Input 2 → [10,20,30],30 → Output 2 → [(10,20)]

# Check if List is Palindrome
# Input 1 → [1,2,1] → Output 1 → True
# Input 2 → [1,2,3] → Output 2 → False

# Find Duplicate Elements in List
# Input 1 → [1,2,2,3] → Output 1 → [2]
# Input 2 → [a,b,a,c] → Output 2 → ['a']

# Find Missing Number in List of 1 to N
# Input 1 → [1,2,4,5], N=5 → Output 1 → 3
# Input 2 → [3,1,2,5], N=5 → Output 2 → 4

def allpairsum(getList, sumValue):
    newList = []

    for i in range(len(getList)):
        for j in range(i+1, len(getList)):
            if getList[i] + getList[j] == sumValue:
                newList.append((getList[i],getList[j]))
    return newList

def isPalindromeList(list):
    if list == list[::-1]:
        return True
    return False

def duplicateElement(list):
    newList = []

    for i in list:
        if list.count(i) > 1 and i not in newList:
            return i
        newList.append(i)

def missingnumbers(list, N):
    missing = []
    for i in range(1,N+1):
        if i not in list:
            missing.append(i)
    return missing


def main():
    Ret, List = None, None
############################################
    List = [1,2,3,4]

    Ret = allpairsum(List, 5)
    print("All Pairs with Given Sum: ",Ret)

    List = [1,2,1]

    Ret = isPalindromeList(List)
    if Ret == True:
        print("its palindrome list.")
    else:
        print("its not an palindrome list.")

    List = ['a','b','a','c']

    Ret = duplicateElement(List)
    print(f"Duplicate element in the list is:{Ret}")

    List = [1,2,4,5]
    Ret = missingnumbers(List,7)
    print(f"The missing number from the list:{List} is:{Ret}")



if __name__ == "__main__":
    main()