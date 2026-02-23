# Access the first, last, and middle elements of a list.

def accessFML(getList):
    last = len(getList) - 1
    mid = int(last/2)

    print("First element is: ",getList[0])
    print("mid element is: ",getList[mid])
    print("last element is: ",getList[last])

def main():
    myList = [10,20,30,4,3,2,7,80,1]

    print(myList)

    accessFML(myList)

if __name__ == "__main__":
    main()