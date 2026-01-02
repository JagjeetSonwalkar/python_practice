class Node:
    def __init__(self, A):
        self.data = A
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None
        self.iCountNode = 0
    
    def addFirst(self, getData):
        
        newn = Node(getData)

        if(self.head == None):
            self.head = newn
        else:
            newn.next = self.head
            self.head = newn
        
        self.iCountNode = self.iCountNode + 1

    def displayLL(self):
        temp = self.head

        while(temp != None):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next
        print("None")

        temp = None
    
    def countNode(self):
        return self.iCountNode
    
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

    # indexing start with 1
    def addAtPosition(self, getPosition, getData):
        newn = Node(getData)

        if(getPosition == 1):
            self.addFirst(getData)
        elif(getPosition == self.iCountNode+1):
            self.addLast(getData)
        else:
            temp = self.head

            for i in range(1, getPosition-1, 1):
                temp = temp.next
            newn.next = temp.next
            temp.next = newn

            self.iCountNode = self.iCountNode + 1
    
    def removeFirst(self):
        if(self.head == None):
            return 
        elif(self.head.next == None):
            del self.head
            self.head = None
        else:
            target = self.head
            self.head = self.head.next
            del target
        
        self.iCountNode = self.iCountNode - 1

    def removeLast(self):
        if(self.head == None):
            return 
        elif(self.head.next == None):
            del self.head
            self.head = None
        else:
            temp = self.head

            while(temp.next.next != None):
                temp = temp.next
            temp.next = None
            
            del temp
        
        self.iCountNode = self.iCountNode - 1

    def removeAtPosition(self, getPosition):
        if(self.head == None or getPosition <= 0):
            return
        
        if(getPosition == 1):
            self.removeFirst()
        elif(getPosition == self.iCountNode):
            self.removeLast()
        else:
            temp = self.head

            for i in range(0, getPosition - 1, 1):
                temp = temp.next
            temp.next = temp.next.next

            temp = None

            self.iCountNode = self.iCountNode - 1

    def clear(self):
        if(self.head == None):
            return 
        else:
            temp = self.head 

            while(temp != None):
                temp = temp.next
                target = temp
                del target
                self.iCountNode = self.iCountNode - 1
            
        self.head = None   
#########################################
def main():
    iRet = 0

    ioption = 0
    data = None
    iPos = 0

    Obj = SinglyLL()

    while(True):
        print("|||||||||||||||||||||||||||||||||||")
        print("0. terminate the program")
        print("1. Count the Total nodes of LL.")
        print("2. display Linked List")
        print("3. Add new element at first.")
        print("4. Add new element at Last.")
        print("5. Add new element at required position(where position start with 1).")
        print("6. delete first element from the Linked List")
        print("7. delete Last element from the Linked List")
        print("8. delete the element from the required position of Linked List")
        print("9. delete all the element from the Linked List")
        print("|||||||||||||||||||||||||||||||||||")
        ioption = int(input("Enter the option: "))
        print("|||||||||||||||||||||||||||||||||||")

        if(ioption == 0):
            print("Program is going to close !!")
            break
        elif(ioption == 1):
            iRet = Obj.countNode()
            print("Total nodes in LL are: ",iRet)
        elif(ioption == 2):
            Obj.displayLL()
        elif(ioption == 3):
            data = input("Enter the data: ")
            Obj.addFirst(data)
        elif(ioption == 4):
            data = input("Enter the data: ")
            Obj.addLast(data)
        elif(ioption == 5):
            iPos = int(input("Enter the position: "))
            data = input("Enter the data: ")
            Obj.addAtPosition(iPos, data)
        elif(ioption == 6):
            data = input("Enter the data: ")
            Obj.removeFirst()

        elif(ioption == 7):
            Obj.removeLast()
        elif(ioption == 8):
            iPos = int(input("Enter the position: "))
            Obj.removeAtPosition(iPos)
        elif(ioption == 9):
            Obj.clear()
        else:
            print("!! Invalid Option, try again a valid option.")

#########################################
if __name__ == "__main__":
    main()