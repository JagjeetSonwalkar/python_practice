#	Find the second largest element in a list

def secondMax(myList):
    max1 = myList[0]
    max2 = myList[1]

    if(len(myList) == 0):
        max2 = myList[0]
    elif(len(myList) == 2):
        if(myList[0] > myList[1]):
            max2 = myList[1]
        else:
            max2 = myList[0]
    else:
        for i in myList:
            if(max1 < i):
                max2 = max1
                max1 = i

            if(i > max2 and i < max1):
                max2 = i
            
    return max2


def main():

    myList = [10, 3, 4,0, 100, 99, 6, 7,101, 9, 1]

    returnValue = 0

    returnValue = secondMax(myList)
    print("Second largest element in a list: ",returnValue)

if __name__ == "__main__":
    main()