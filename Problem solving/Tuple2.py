## PROBLEM STATEMNT ##

# Unpack Tuple into Variables
# Input 1 → (1,2,3) → Output 1 → a=1, b=2, c=3
# Input 2 → ('x','y') → Output 2 → a='x', b='y'

#  Nested Tuple Access
# Input 1 → (1,(2,3),4), index [1][0] → Output 1 → 2
# Input 2 → ('a',('b','c'),'d'), index [1][1] → Output 2 → 'c'

# Tuple Immutability Test
# Input 1 → (1,2,3), try tuple[0]=10 → Output 1 → Error: TypeError
# Input 2 → ('a','b'), try tuple[1]='x' → Output 2 → Error: TypeError

# Find Max and Min in Tuple

# Reverse a Tuple
# Input 1 → (1,2,3) → Output 1 → (3,2,1)
# Input 2 → ('a','b','c') → Output 2 → ('c','b','a')

# Multiply Each Element by N (using comprehension)
# Input 1 → (1,2,3), N=2 → Output 1 → (2,4,6)
# Input 2 → (4,5), N=3 → Output 2 → (12,15)

# Concatenate Multiple Tuples
# Input 1 → (1,2),(3,4),(5,) → Output 1 → (1,2,3,4,5)
# Input 2 → ('a','b'),('c',) → Output 2 → ('a','b','c')

#  Find Length of Each Nested Tuple
# Input 1 → ((1,2),(3,4,5)) → Output 1 → [2,3]
# Input 2 → (('a','b'),('c',)) → Output 2 → [2,1]

######################
def unpackTuple(tuple):
    variables = {}
    for i, var in enumerate(tuple):
        variables[f'var{i+1}'] = var
    for variblename, variablevalue in variables.items():
        print(f"{variblename} = {variablevalue}")
        
def nestedTupleAccess(Tup, start, end):
    for i in range(start,end+1):
        print(Tup[i],end=" ")

def maxmin(tup):
    tupList = []
    for i in tup:
        if isinstance(i, tuple):
            tupList.extend(i)
        else:
            tupList.append(i)

    max, min = tupList[0], tupList[0]
    for i in tupList:
        if i > max:
            max = i
        elif i < min:
            min = i
    return max, min

def sumAll(tup):
    iSum = 0
    newList = []

    for i in tup:
        if isinstance(i, tuple):
            newList.extend(i)
        else:
            newList.append(i)

    for i in newList:
        iSum += i
    return iSum

def reveseTuple(tup):
    for i in range(len(tup)-1,-1,-1):
        print(tup[i],end=" ")
    print()

def multTuple(tup, N):
    result = []
    for i in tup:
        if isinstance(i, tuple):
            result.append(multTuple(i, N))
        else:
            result.append(i * N)
    return result

def concenateTuple(tup):
    result = []
    for i in tup:
        if isinstance(i, tuple):
            result.extend(i)
        else:
            result.append(i)
    result = tuple(result)
    return result

def nestedTupleLen(tup):
    result = []
    for i in tup:
        if isinstance(i,tuple):
            result.append(len(i))
    return result


## main() function ##
def main():
    ## varibale ##
    Ret, Ret2 = None, None
    iStart, iEnd = 0, 0
    ##############

    # Convert Tuple to List
    tup = (1,2,3,4,5)
    Ret = list(tup)
    print(f"{tup} type: {type(tup)}, {Ret} type:{type(Ret)}")
    
    # Unpack Tuple into Variables
    unpackTuple(tup)

    #  Nested Tuple Access1
    tup = (1,(2,0,3),5,6,(4,2))
    print("Enter the start and ending value to ascess the tuple: ")
    iStart = int(input())
    iEnd = int(input())
    nestedTupleAccess(tup, iStart, iEnd)
    
    # Tuple Immutability Test
    # tup[0] = 99   # ERROR
    # print(tup)

    
    Ret, Ret2 = maxmin(tup)
    print(f"From the tuple:{tup}, the max is {Ret} & the min is {Ret2}")

    Ret = sumAll(tup)
    print(f"The sum of the tuple is {tup} & sum is {Ret}")

    reveseTuple(tup)

    Ret = multTuple(tup, 2)
    print(f"The multipal of tuple by 2 is: {Ret}")

    tup = (1,(2,0,3),5,6,(4,2))

    Ret = concenateTuple(tup)
    print(f"The tuple before:{tup} & orignal:{Ret}")

    tup = ((2,0,3),(4,2),(1,))
    Ret = nestedTupleLen(tup)
    print(f"Tuple:{tup} and its nested tuple lenght:{Ret}")

if __name__ == "__main__":
    main()
