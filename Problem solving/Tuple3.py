## PROBLEM STATEMNT ##

# Convert Tuple of Strings to Single String
# Input 1 → ('a','b','c') → Output 1 → 'abc'
# Input 2 → ('Hello','World') → Output 2 → 'HelloWorld'

# Convert Tuple of Numbers to String Numbers
# Input 1 → (1,2,3) → Output 1 → ('1','2','3')
# Input 2 → (10,20) → Output 2 → ('10','20')

# Find Index of Max Element
# Input 1 → (3,5,2) → Output 1 → 1
# Input 2 → (10,20,15) → Output 2 → 1

# Find Index of Min Element
# Input 1 → (3,5,2) → Output 1 → 2
# Input 2 → (10,5,20) → Output 2 → 1

## END ##

def toSingleString(tup):
    result = ""

    for i in tup:
        if isinstance(i, tuple):
            result += toSingleString(i)  
        else:
            result += str(i)

    return result

def toStringNumber(tup):
    result = []
    for i in tup:
        if isinstance(i, tuple):
            result.append(tuple(str(x) for x in i))
        else:
            result.append(str(i))
    print(result)

def maxElementIndex(tup):
    maxElement = tup[0]
    maxIndex = 0

    for i in range(len(tup)):
        if isinstance(tup[i], tuple):
            maxElement = maxElementIndex(tup[i])
        else:
            if tup[i] > maxElement:
                maxIndex = tup.index(tup[i])
                maxElement = tup[i]
    return maxIndex

def minElementIndex(tup):
    minElement = tup[0]
    minIndex = 0

    for i in range(len(tup)):
        if isinstance(tup[i], tuple):
            minElement = minElementIndex(tup[i])
        else:
            if tup[i] < minElement:
                minIndex = tup.index(tup[i])
                minElement = tup[i]
    return minIndex



## main() function ##
def main():
    ## varibale ##
    Ret = None
    ##############
    tup = ('a','b',('i','h','g'),'c',('d','e','f'))
    Ret = toSingleString(tup)
    print(Ret)

    tup2 = (1,2,(3,4,0),9,(8,7,6))
    toStringNumber(tup2)

    tup = (1,0,(4,56,78),99,9)
    Ret = maxElementIndex(tup)
    print("Max element index is:",Ret)

    Ret = minElementIndex(tup)
    print("Min element index is:",Ret)   

if __name__ == "__main__":
    main()
