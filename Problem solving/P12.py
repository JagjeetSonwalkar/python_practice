# Merge two sorted lists into one sorted list

def mergeList(getList1, getList2):
    newList = []

    for i in getList1:
        newList.append(i)
    for i in getList2:
        newList.append(i)
    
    newList.sort()

    return newList
      

def main():

    myList1 = [1, 2, 3, 2, 3, 4, 5]
    myList2 = [6, 8, 0, 7, 2, 0, 9]

    myList1.sort()
    myList2.sort()

    print(myList1,myList2)

    ret = []
    ret = mergeList(myList1, myList2)
    
    print("merge of two sorted list: ")
    print(ret)

if __name__ == "__main__":
    main()