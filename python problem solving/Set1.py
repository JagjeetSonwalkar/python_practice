
def unionX(set1, set2):
    result = set()
    for i in set1:
            result.add(i)
    for i in set2:
            result.add(i)
    return result

def intersectionX(s1, s2):
    result = set()

    for i in s1:
        if i in s2:
            result.add(i)
    return result 

def differnceX(set1, set2):
    result = set()

    for i in set1:
        if i not in set2:  
            result.add(i)
    return result 

def symmetricDifferenceX(set1, set2):
    result = set()

    for i in set1:
        if i not in set2:
            result.add(i)
    for i in set2:
        if i not in set1:
            result.add(i)
    return result

def main():
    # Create a Set and Print It
    name = set()
    name = {"hardik", "MS", "Python"}
    print("Type:",type(name)," Set:",name)

    # Add Element to a Set
    name.add("Rohit")
    name.add("Virat")
    name.add("Bum Bum")

    print("set:",name)

    # Remove Element from a Set
    name.remove("MS")

    print("set:",name)

    # Check if Element Exists in a Set
    if "GOD" in name:
        print("element exists in set")
    else:
        print("element doesnt exists")

    # Find Length of a Set
    print("lenght of set is:",len(name))

    # Convert List to Set (Remove Duplicates
    myList = [1,2,3,2,3,4,5,4,5,6]
    numSet = set(myList)
    print("List:",myList," ,Set:",numSet)

    ### Varibale  ###
    Ret = None
    set1 = {1,2,}
    set2 = {2,3}
    

    # Union of Two Sets
    Ret = unionX(set1, set2)
    print(f"{set1} U {set2} = {Ret}")

    # Intersection of Two Sets
    Ret = intersectionX(set1, set2)
    print(f"Intersection of two set {set1} & {set2} = {Ret}")

    # Difference of Two Sets
    Ret = differnceX(set1, set2)
    print(f"The differnece of two set is {set1} & {set2} = {Ret}")

    # Symmetric Difference of Two Sets
    Ret = symmetricDifferenceX(set1, set2)
    print(f"The Symmetric Difference of two set is {set1} & {set2} = {Ret}")

    

if __name__ == "__main__":
    main()