#  Get Value with Default (get method)
# Input 1 → {'a':1}, key 'b', default 0 → Output 1 → 0
# Input 2 → {1:'x'}, key 2, default 'y' → Output 2 → 'y'

# Remove Item and Return Value (pop)
# Input 1 → {'a':1,'b':2}, pop 'a' → Output 1 → 1
# Input 2 → {1:'x',2:'y'}, pop 2 → Output 2 → 'y'

# Pop Item (Last Inserted)
# Input 1 → {'a':1,'b':2} → Output 1 → ('b',2)
# Input 2 → {1:'x',2:'y'} → Output 2 → (2,'y')

# Merge Dictionaries Using | Operator (Python 3.9+)
# Input 1 → {'a':1} | {'b':2} → Output 1 → {'a':1,'b':2}
# Input 2 → {1:'x'} | {2:'y'} → Output 2 → {1:'x',2:'y'}

# Reverse Key-Value Pairs (Swap)
# Input 1 → {'a':1,'b':2} → Output 1 → {1:'a',2:'b'}
# Input 2 → {1:'x',2:'y'} → Output 2 → {'x':1,'y':2}

def getValuewithdefault(dictx, key, default):
    return dictx.get(key, default)

def removeXreturnY(dictx, key):
    result = None
    if key in dictx:
        result = dictx.pop(key)
        return result
    else:
        print("The key not exists !")
        return None

def popLastItem(dictx):
    return dictx.popitem()

def mergerDict(dict1, dict2):
    return dict1 | dict2

def swapKeyValue(dictx):
    keyList = list(dictx.keys())
    valueList = list(dictx.values())
    resultDict = {}

    for i in range(len(dictx)):
        resultDict.update({valueList[i] : keyList[i]})

    return resultDict

def main():
    dicts = dict()
    Ret = None
    key = None
    #############
    dicts = {'a':1,'b':2, 'c':3}

    Ret = getValuewithdefault(dicts, 'd', 10)
    print(Ret)

    key = input("Enter the key to remove the item and return the value: ")
    Ret = removeXreturnY(dicts, key)
    print(f"The value of key {key} is {Ret} & The dict is {dicts}")

    Ret = popLastItem(dicts)
    print(f"The last item was {Ret} & The dict is {dicts}")

    dict1 = {'b':2, 'j':1, 'z':100}
    Ret = mergerDict(dicts, dict1)
    print(Ret)

    Ret = swapKeyValue(dicts)
    print(f"Before swap {dicts} & After swap {Ret}")


if __name__ == "__main__":
    main()