'''
    Linked list is data structure 
    operations on LL: Insertion(At beginning, At end, At a specfic position), Deletion(At beginning, At end, At a specfic position),
    Traversal(Displaying elements, Searching),size of linked list,  Updating(Modification), Merging, Reversal
'''

# Node of LinkedList
class Node:
    def __init__(self, A):
        self.data = A 
        self.next = None

# LinkedList
class LinkedList:

    # Constructor
    def __init__(self):
        self.head = None
        self.iCountNode = 0

    # Insertion At beginning
    def add(self, getData):
        newn = Node(getData)

        if(self.head == None):
            self.head = newn
        else:
            newn.next = self.head
            self.head = newn

        self.iCountNode = self.iCountNode + 1
        return True

    # Insertion At end
    def addLast(self, getData):
        newn = Node(getData)

        if(self.head == None):
            self.head = newn
        else:
            temp = self.head

            while(temp.next != None):
                temp = temp.next
            temp.next = newn

            temp = None

        self.iCountNode = self.iCountNode + 1
        return True

    # Insertion at specfic position
    def addAtPos(self, getPos, getData):

        if(getPos <= 0 or getPos > self.iCountNode+1):
            return "Invalid Position"

        if(getPos == 1):
            self.add(getData)
        elif(getPos == self.iCountNode+1):
            self.addLast(getData)
        else:
            newn = Node(getData)

            temp = self.head

            for i in range(1, getPos-1, 1):
                temp = temp.next
            newn.next = temp.next
            temp.next = newn

            temp = None
            self.iCountNode = self.iCountNode + 1

            return True
    
    # Remove - At beginning
    def remove(self):
        if(self.head == None):
            return "List is already empty, Unable to remove element !"

        if(self.head.next == None):
            self.head = None
        else:
            self.head = self.head.next
        
        self.iCountNode = self.iCountNode - 1

        return True

    # Remove - At end
    def removeLast(self):
        if(self.head == None):
            return "List is already empty, Unable to remove element !"

        if(self.head.next == None):
            self.head = None
        else:
            temp = self.head

            while(temp.next.next != None):
                temp = temp.next
            temp.next = None

            temp = None
        
        self.iCountNode = self.iCountNode - 1

        return True

    # Remove = At specfic position
    def removeAtPos(self, getPos):
        if(self.head == None):
            return "List is already empty, Unable to remove"

        if(getPos <= 0 or getPos > self.iCountNode):
            return "Invalid Position !"

        if(getPos == 1):
            self.remove()
        elif(getPos == self.iCountNode):
            self.removeLast()
        else:
            temp = self.head

            for i in range(1, getPos-1, 1):
                temp = temp.next
            temp.next = temp.next.next

            self.iCountNode = self.iCountNode - 1
            temp = None
            return True

    # Traversal - Displaying elements
    def display(self):
        if(self.head == None):
            print("List is empty !")
            return

        temp = self.head

        while(temp != None):
            print(temp.data,"->",end=" ")
            temp = temp.next
        print('NULL',end=" ")
        print()

        temp = None

    # Traversal - searching
    def search(self,getData):
        if(self.head == None):
            return "List is empty !"
        
        temp = self.head
        while(temp != None):
            if(temp.data == getData):
                return True
            temp = temp.next

        temp = None
        return False

    # Traversal - size of linked list
    def size(self):
        if(self.head == None):
            return "Empty"

        return self.iCountNode
###########################################
def main():

    # Variable
    Obj = LinkedList()
    iRet = None
    data = None
    iOption = 0
    iPos = 0

    while True:
        print("######################################")
        print("0. exit from the program.")
        print("1. Insert data at beginning.")
        print("2. Insert data at end.")
        print("3. Insert data at specfic position.")
        print("4. Remove data from beginning.")
        print("5. Remove data from end.")
        print("6. Remove data from specific position.")
        print("7. Display the Linked List")
        print("8. Search an element is present or not.")
        print("9. check the size of list.")
        print("######################################")
        print()
        iOption = int(input("Enter your option: "))
        print("######################################")

        if(iOption == 0):
            print("Application is closed.")
            break
        elif(iOption == 1):
            data = input("Enter the data: ")
            iRet = Obj.add(data)

            if(iRet == True):
                print("Data inseted succesfully.")
            else:
                print("fail to insert the data !!")
        elif(iOption == 2):
            data = input("Enter the data: ")
            iRet = Obj.addLast(data)

            if(iRet == True):
                print("Data inseted succesfully.")
            else:
                print("fail to insert the data !!")
        elif(iOption == 3):
            iPos = int(input("Enter the position: "))
            data = input("Enter the data: ")

            iRet = Obj.addAtPos(iPos, data)

            if(iRet == True):
                print("Data inseted succesfully.")
            else:
                print("fail to insert the data !!")
        elif(iOption == 4):
            iRet = Obj.remove()
            if(iRet == True):
                print("Data remove succesfully.")
            else:
                print("fail to remove the data !!")
        elif(iOption == 5):
            iRet = Obj.removeLast()
            if(iRet == True):
                print("Data remove succesfully.")
            else:
                print("fail to remove the data !!")
        elif(iOption == 6):
            iPos = int(input("Enter the position: "))

            iRet = Obj.removeAtPos(iPos)
            if(iRet == True):
                print("Data remove succesfully.")
            else:
                print("fail to remove the data !!")
        elif(iOption == 7):
            Obj.display()
        elif(iOption == 8):
            data = input("Enter the data to search: ")

            iRet = Obj.search(data)

            if(iRet == True):
                print("Data is present is List")
            else:
                print("Data is not present in List !")
        elif(iOption == 9):
            iRet = Obj.size()

            print("Size of list is: ",iRet)
        else:
            print("Invalid option, pls enter a valid option.")
###########################################
if __name__ == "__main__":
    main()