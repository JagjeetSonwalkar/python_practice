## PROBLEM STATEMNT ##

# Convert Tuple to Dictionary (Pairwise)
# Input 1 → (('a',1),('b',2)) → Output 1 → {'a':1,'b':2}
# Input 2 → (('x',10),('y',20)) → Output 2 → {'x':10,'y':20}

# Tuple Rotation (Right by N)
# Input 1 → (1,2,3,4),2 → Output 1 → (3,4,1,2)
# Input 2 → ('a','b','c'),1 → Output 2 → ('c','a','b')

#  Find All Duplicate Elements in Tuple
# Input 1 → (1,2,2,3) → Output 1 → (2,)
# Input 2 → ('a','b','a') → Output 2 → ('a',)

# Count Occurrences of Each Element in Tuple
# Input 1 → (1,2,2,3) → Output 1 → {1:1,2:2,3:1}
# Input 2 → ('a','b','a') → Output 2 → {'a':2,'b':1}

## END ##

def rotate(tup, N):
    newTuple = ()
    newTuple = tup[N:] + tup[:N]
    return newTuple

def findDuplicate(tup):
    myList = []
    duplicate = []

    for i in tup:
        if isinstance(i, tuple):
            for x in i:
                myList.append(x)
        else:
            myList.append(i)

    for i in myList:
        if myList.count(i) > 1 and i not in duplicate:
            duplicate.append(i)
    return duplicate

def countOccurnece(tup):
    myDict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    result = {}

    myList = []
    for i in tup:
        if isinstance(i, tuple):
            for x in i:
                myList.append(x)
        else:
            myList.append(i)

    for i in myList:
        if i in myDict.keys():
            value = myDict[i] + 1
            myDict.update({i : value})

    for i in myDict:
        if myDict[i] != 0:
            result.update({i:myDict[i]})
    
    return result

## main() function ##
def main():
    ## varibale ##
    Ret = None
    iValue = 0
    ##############
    myTuple = (('a',1),('b',2))

    Ret = dict(myTuple)
    print("Converted into dict:",Ret)

    myTuple = (1,2,3,4)
    iValue = int(input("Enter the n position to rotated: "))
    Ret = rotate(myTuple, iValue)
    print(Ret)

    myTuple = (0,(1,2,3,4),2,(1,4),9)
    Ret = findDuplicate(myTuple)
    print(f"The original tuple {myTuple} & the duplicate elements are {Ret}")

    Ret = countOccurnece(myTuple)
    print("Occurnece of each element in tuple:",Ret)
      

if __name__ == "__main__":
    main()
