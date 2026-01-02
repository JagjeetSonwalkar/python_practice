# Find Common Elements in Multiple Sets
# Input 1 → {1,2,3}, {2,3,4}, {3,5} → Output 1 → {3}
# Input 2 → {'a','b'}, {'b','c'}, {'b','d'} → Output 2 → {'b'}

# Union of Multiple Sets
# Input 1 → {1,2},{2,3},{3,4} → Output 1 → {1,2,3,4}
# Input 2 → {'a'},{ 'b','c'}, {'a','d'} → Output 2 → {'a','b','c','d'}

# Symmetric Difference of Multiple Sets
# Input 1 → {1,2,3}, {2,3,4}, {3,4,5} → Output 1 → {1,5}
# Input 2 → {'a','b'}, {'b','c'}, {'a','d'} → Output 2 → {'c','d'}

def commonElement(s1):
    common = set()
    common = s1[0]

    for subset in s1[1:]:
        temp = set()
        for i in common:
            if i in subset:
                temp.add(i)
        common = temp
    return common

def unionMutipleSet(set1):
    result = set()

    for subset in set1:
        for i in subset:
            if i not in result:
                result.add(i)
    return result

def symmetricDifference(sett):
    result = set()

    for subset in sett:
        temp = set()
        for i in subset:
            if i in result:
                result.remove(i)
            else:
                temp.add(i)
        for j in temp:
            result.add(j)
    
    return result


def main():
    Ret = None
    setX = set()

    setX = [{1,2,3},{2,3,4},{3,5}]

    Ret = commonElement(setX)
    print(f"The common elements in multiple set's is {Ret}")

    Ret = unionMutipleSet(setX)
    print(f"Union of Multiple Sets is {Ret}")

    Ret = symmetricDifference(setX)
    print(f"Symmetric Difference of Multiple Sets is {Ret}")
    


if __name__ == "__main__":
    main()