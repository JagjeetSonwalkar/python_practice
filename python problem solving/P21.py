# Replace all occurrences of an element with another.

def replaceElement(getList, getExistsValue, getUpdateValue):
    
    for i in range(len(getList)):
        if(getList[i] == getExistsValue):
            getList[i] = getUpdateValue

def main():
    myList = [10, 20, 20, 30, 10, 20, 50, 60, 50]

    print("Orignal list: ",myList)

    replaceElement(myList, 10, 100)
    replaceElement(myList, 20, 2000)

    print("Updated list: ",myList)
    

if __name__ == "__main__":
    main()