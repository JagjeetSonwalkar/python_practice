class Node:
    def __init__(self, A):
        self.data = A 
        self.next = None
        self.prev = None

class DoublyLinkedList:
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

        print("None <=>",end="")
        while(temp != None):
            print("| ",temp.data," |<=>",end="")
            temp = temp.next
        print("None",end="")
        print()

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
            newn.prev = temp
            temp.next = newn

            temp = None
        
        self.iCountNode = self.iCountNode + 1

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
            temp.next.prev = newn
            newn.next = temp.next
            temp.next = newn
            newn.prev = temp

            self.iCountNode = self.iCountNode + 1

    def removeFirst(self):
        if(self.head == None and self.tail == None):
            return "Linked List is empty"

        if(self.head.next == None):
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.iCountNode = self.iCountNode - 1

    def removeLast(self):
        if(self.head == None and self.tail == None):
            return "Linked List is empty"

        if(self.head.next == None):
            self.head = None
        else:
            temp = self.head

            while(temp.next.next != None):
                temp = temp.next
            temp.next = None
        self.iCountNode = self.iCountNode - 1    

    def removeAtPosition(self, getPosition):
        if(self.head == None and self.tail == None):
            return "Linked List is empty"
        
        if(getPosition == 1):
            self.removeFirst()
        elif(getPosition == self.iCountNode):
            self.removeLast()
        else:
            temp = self.head

            for i in range(1, getPosition, 1):
                temp = temp.next
            temp.next.prev = temp.prev
            temp.prev.next = temp.next  

            temp = None 
            self.iCountNode = self.iCountNode -1
###################################
def main():
    Obj = DoublyLinkedList()
    iRet = 0

    Obj.addFirst(10)
    Obj.addFirst(20)
    Obj.addFirst(30)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.addLast(123)
    Obj.addLast(311)
    Obj.addLast(232)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.addAtPosition(1,111)
    Obj.addAtPosition(8, 999)
    Obj.addAtPosition(4, 0000)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.removeFirst()
    Obj.removeLast()

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.removeAtPosition(1)
    Obj.removeAtPosition(6)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.removeAtPosition(2)
    Obj.removeAtPosition(3)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)



###################################

if __name__ == "__main__":
    main()