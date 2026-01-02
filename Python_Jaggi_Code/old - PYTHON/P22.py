# Remove all even numbers from a list
# Remove all odd numbers from a list

def removeEven(getList):
    return [x for x in getList if x % 2 != 0]

def removeOdd(getList):
    return [x for x in getList if x % 2 == 0]

def main():
    Ret = 0

    myList = [2,1,4,3,6,5,8,7,9,0,1,2,3,4,5,6,7,8,9]

    print("Orignal list: ",myList)

    myList = removeEven(myList)
    print("List after removing even elements: ",myList)

    print("Orignal list: ",myList)

    myList = removeOdd(myList)
    print("List after removing odd elements: ",myList)

if __name__ == "__main__":
    main()