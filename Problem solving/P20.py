# Print even numbers from a list
# Print odd numbers from a list.

def checkEven(getList):
    evenList = []
    for i in getList:
        if(i % 2 == 0):
            evenList.append(i)
    return evenList

def checkOdd(getList):
    oddList = []
    for i in getList:
        if(i % 2 != 0):
            oddList.append(i)
    return oddList


def main():
    Ret = 0

    myList = [1,2,3,4,5,6,7,8,9,0]

    Ret = checkEven(myList)
    print("From list {0} \t Even elements are {1}.".format(myList,Ret))

    Ret = checkOdd(myList)
    print("From list {0} \t Odd elements are {1}.".format(myList,Ret))

    

if __name__ == "__main__":
    main()