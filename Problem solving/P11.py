# Merge two lists into one.

def mergeList(getList1, getList2):
    newList = []

    for i in getList1:
        newList.append(i)
    for i in getList2:
        newList.append(i)

    return newList

# def mergeList(getList1, getList2):
#     newList = []

#     for i in getList1, getList2:
#         newList.append(i)

#     return newList
        

def main():

    myList1 = [1, 2, 3, 2, 3, 4, 5]
    myList2 = [6, 8, 0, 7, 2, 0, 9]

    print(myList1,myList2)

    ret = []
    ret = mergeList(myList1, myList2)
    
    print("merge of two list: ")
    print(ret)

if __name__ == "__main__":
    main()