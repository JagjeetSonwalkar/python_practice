# Sort a list without using the built-in sort() method.

def sortList(getList):

    for i in range(len(getList)):
        for j in range(len(getList)-i-1):
            if(getList[j] > getList[j+1]):
                temp = getList[j+1]
                getList[j+1] = getList[j]
                getList[j] = temp
    return getList

def main():
    Ret = 0

    myList = [2,1,4,3,6,5,8,7,9,0,1,2,3,4,5,6,7,8,9]

    print("Orignal list: ",myList)

    myList = sortList(myList)

    print("Sorted List: ", myList)

if __name__ == "__main__":
    main()