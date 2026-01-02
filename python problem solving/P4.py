# Insert an element at index 2.
# Remove an element by value
# Remove an element by index
# Reverse a list using slicing

def reverseList(getList):
    for i in range((len(getList)-1),-1,-1):
        print(getList[i])

def main():
    myList = [10,20,30,2,3,4,3,45]

    print("orginal: ",myList)

    myList.insert(2, 1111)  # Insert an element at index 2.
    print(myList)

    myList.remove(45)   # Remove an element by value
    print(myList)

    myList.pop(7)   # Remove an element by index
    print(myList)

    print("using user derfined function: ")
    reverseList(myList) # Reverse a list

    reversedList = myList[::-1] # # Reverse a list using slicing
    print("Using slicing\n",reversedList)

    print("Using inbuild method: ")
    myList.reverse()    # Reverse a list

    print(myList)

    

    

    




if __name__ == "__main__":
    main()