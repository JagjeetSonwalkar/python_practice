# Check if a list is palindrome

def checkPalindrome(getList):
    bRet = False 

    newList1 = []
    newList2 = []

    newList1 = getList
    newList2 = getList[::-1]

    print(newList1)
    print(newList2)

    if(newList1 == newList2):
        bRet = True
    
    return bRet

def main():

    myList1 = [1, 2, 3, 2, 1]
    myList2 = [2, 5 , 1, 0, 0, 1 , 5]

    Ret = 0

    Ret = checkPalindrome(myList1)

    if(Ret == True):
        print("List is palindrome")
    else:
        print("List is NOT palindrome")

if __name__ == "__main__":
    main()