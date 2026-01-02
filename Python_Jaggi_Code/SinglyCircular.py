
class Node:
    def __init__(self, A):
        self.data = A 
        self.next = None

class SinglyCircularLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.iCountNode = 0

    def addFirst(self, getData):
        newn = Node(getData)

        if(self.head == None and self.tail == None):
            self.head = newn
            self.tail = newn   

            self.tail.next = self.head  
        else:
            newn.next = self.head
            self.head = newn

            self.tail.next = self.head

        self.iCountNode = self.iCountNode + 1

    def displayLL(self):

        temp = self.head
        temp2 = self.tail

        print("head->",end="")
        for i in range(1, self.iCountNode+1, 1):
            print("| ",temp.data," |->",end="")
            temp = temp.next
        print("head")

    def countNode(self):
        return self.iCountNode

    def addLast(self, getData):

        newn = Node(getData)

        if(self.head == None and self.tail == None):
            self.head = newn
            self.tail = newn   

            self.tail.next = self.head  
        else:
            self.tail.next = newn
            self.tail = newn
            
            self.tail.next = self.head 

        self.iCountNode = self.iCountNode + 1

    def addAtPosition(self, getPosition, getData):

        if(getPosition <= 0 or getPosition > self.iCountNode+1):
            return "Invalid Position !!"

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
        
            self.tail.next = self.head 

            self.iCountNode = self.iCountNode + 1

    def removeFirst(self):

        if(self.head == None and self.tail == None):
            return "NULL"
        
        if(self.head.next == self.tail.next):
            self.head = None
            del head
        else:
            self.head = self.head.next
        
        self.tail.next = self.head 

        self.iCountNode = self.iCountNode - 1
    
    def removeLast(self):
        if(self.head == None and self.tail == None):
            return "NULL"
        
        if(self.head.next == self.tail.next):
            self.head = None
            del head
        else:
            temp = self.head
            while(temp.next != self.tail):
                temp = temp.next
            temp.next = None
            self.tail = temp
        
        self.tail.next = self.head 

        self.iCountNode = self.iCountNode - 1

    def removeAtPosition(self, getPosition):
        if(getPosition <= 0 or getPosition > self.iCountNode):
            return "Invalid Position !!"

        if(getPosition == 1):
            self.removeFirst()
        elif(getPosition == self.iCountNode):
            self.removeLast()
        else:
            temp = self.head

            for i in range(1, getPosition-1, 1):
                temp = temp.next
            temp.next = temp.next.next

            self.tail.next = self.head 

            self.iCountNode = self.iCountNode - 1

    def clear(self):
        temp = self.head
        temp2 = self.tail

        print("head->",end="")
        for i in range(1, self.iCountNode+1, 1):
            temp = temp.next
            target = temp
            del target
            self.iCountNode = self.iCountNode - 1
        print("head")

        self.head = None

###################################
def main():
    Obj = SinglyCircularLL()
    iRet = 0

    Obj.addFirst(10)
    Obj.addFirst(20)
    Obj.addFirst(30)

    Obj.displayLL()

    Obj.addLast(123)
    Obj.addLast(311)
    Obj.addLast(232)

    Obj.displayLL()

    Obj.addAtPosition(1, 100)
    Obj.addAtPosition(4, 111)
    Obj.addAtPosition(9, 2525)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.removeFirst()

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.removeLast()

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.removeAtPosition(4)
    Obj.removeAtPosition(3)
    Obj.removeAtPosition(1)
    Obj.removeAtPosition(4)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.clear()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)




###################################

if __name__ == "__main__":
    main()