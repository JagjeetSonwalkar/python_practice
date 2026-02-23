
# find the lowest element from the list

def find_min(getList):

    minValue = getList[0]

    for i in getList:
        if(minValue > i):
            minValue = i
    return minValue

def main():
    myList = [7, 12, 9, 4, 11, 8]

    print(myList)
    
    iRet = find_min(myList)

    print("Lowest element is: ",iRet)

if __name__ == "__main__":
    main()