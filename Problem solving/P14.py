# Rotate a list by k positions

def rotate(getList, getindex):
    getindexValue = getindex - 1

    print("[",end="")
    for i in range(getindexValue, len(getList), 1):
        print(getList[i],end=", ")
    for i in range(0, getindexValue, 1):
        print(getList[i],end=", ")
    print("]",end="")
    print()

def main():

    myList1 = [1,2,3,4,5,6,7,8,9,0]

    print(myList1)

    rotate(myList1,8)

if __name__ == "__main__":
    main()