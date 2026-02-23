# Find Keys with Maximum Value
# Input 1 → {'a':10,'b':20} → Output 1 → 'b'
# Input 2 → {1:5,2:15,3:15} → Output 2 → [2,3]

# Find Keys with Minimum Value
# Input 1 → {'a':10,'b':20} → Output 1 → 'a'
# Input 2 → {1:5,2:15,3:5} → Output 2 → [1,3]

# Count Frequency of Elements in a List Using Dict
# Input 1 → [1,2,2,3] → Output 1 → {1:1,2:2,3:1}
# Input 2 → ['a','b','a'] → Output 2 → {'a':2,'b':1}

#  Filter Dictionary by Value
# Input 1 → {'a':10,'b':20}, keep values >15 → Output 1 → {'b':20}
# Input 2 → {1:5,2:15,3:10}, keep values >=10 → Output 2 → {2:15,3:10}

# Dictionary Comprehension (Square Numbers)
# Input 1 → [1,2,3] → Output 1 → {1:1,2:4,3:9}
# Input 2 → [2,3,4] → Output 2 → {2:4,3:9,4:16}

# Merge Two Dictionaries with Summing Values of Same Keys
# Input 1 → {'a':1,'b':2},{'a':3,'c':4} → Output 1 → {'a':4,'b':2,'c':4}
# Input 2 → {1:10,2:20},{2:5,3:15} → Output 2 → {1:10,2:25,3:15}

# Find Dictionary Keys Present in Another Dictionary
# Input 1 → {'a':1,'b':2},{'b':20,'c':30} → Output 1 → ['b']
# Input 2 → {1:10,2:20},{2:5,3:15} → Output 2 → [2]

# Find Dictionary Values Present in Another Dictionary
# Input 1 → {'a':1,'b':2},{'x':2,'y':3} → Output 1 → [2]
# Input 2 → {1:5,2:10},{3:10,4:15} → Output 2 → [10]

def maxValue(dictx):
    maxValue = list(dictx.values())[0]
    maxKeys = []

    for i in dictx.values():
        if i > maxValue:
            maxValue = i
    for k, v in dictx.items():
        if v == maxValue:
            maxKeys.append(k)
    return maxKeys

def minValue(dictx):
    minValue = list(dictx.values())[0]
    minKeys = []

    for i in dictx.values():
        if i < minValue:
            minValue = i
    for k, v in dictx.items():
        if v == minValue:
            minKeys.append(k)
    return minKeys

def countFrequencylist(list):
    resultDict = {}
    
    for i in list:
        if i not in resultDict.keys():
            resultDict.update({i:1})
        elif i in resultDict.keys():
            value = resultDict[i] + 1
            resultDict.update({i:value})
    return resultDict

def filterbyValue(dict, value):
    resultDict = {}

    for k, v in dict.items():
        if v >= value:
            resultDict.update({k:v})
    return resultDict

def dictComprehension(dictx):
    result = {}

    for k,v in dictx.items():
        result.update({k:v**2})
    
    return result
        
def MergeDictionarieswithSumming(dict1, dict2):
    result = { }
    result = dict1

    for k, v in dict2.items():
        if k not in result.keys():
            result.update({k:v})
        elif k in result.keys():
            value = v + result[k]
            result.update({k:value})
    return result

def keysinAnotherDict(dict1, dict2):
    result = list()

    for i in dict1.keys():
        if i in dict1.keys() and i in dict2.keys():
            result.append(i)
    return result

def valuesinAnotherDict(dict1, dict2):
    result = []

    for i in dict1.values():
        if i in dict1.values() and i in dict2.values():
            result.append(i)
    return result

def main():
    Ret = None
    iValue = 0
    list = [1,2,2,3,4,7,4,2]
    dict = {'a':10, 'b':20, 'c':30, 'd':1, 'e':99, 'f':99}

    Ret = maxValue(dict)
    print(f"{Ret} are Keys with Maximum Value.")

    Ret = minValue(dict)
    print(f"{Ret} Keys with Minimum Value")

    Ret = countFrequencylist(list)
    print(f"list: {list} & the count occurence of element {Ret}")

    iValue = int(input("Enter the value to filer the dict: "))
    Ret = filterbyValue(dict, iValue)
    print(f"Before dict {dict} & After dict {Ret}")

    Ret = dictComprehension(dict)
    print(f"Before dict {dict} & After dict {Ret}")

    dictxx, dictyy = {}, {}

    dictxx = {'a':10, 'b':20, 'c':30, 'd':1, 'e':99, 'f':99}
    dictyy = {'a':10, 'b':20, 'c':30, 'd':1, 'x':1, 'y':88}

    Ret = MergeDictionarieswithSumming(dictxx, dictyy)
    print(f"dictx {dictxx}\ndicty {dictyy}\nMerge Two Dictionaries with Summing Values of Same Keys {Ret}")

    Ret = keysinAnotherDict(dictxx, dictyy)
    print(f"{Ret} Dictionary Keys Present in Another Dictionary")

    Ret = valuesinAnotherDict(dictxx, dictyy)
    print(f"{Ret} Values Present in Another Dictionary")


if __name__ == "__main__":
    main()