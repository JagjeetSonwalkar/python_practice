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
            print(temp.data,end=" ")
            temp = temp.next
        print("->None")

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

            temp = None
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
            target = temp.next
            temp.next = None
            del target
            
            temp = None
        
        self.iCountNode = self.iCountNode - 1

    def removeAtPosition(self, getPosition):
        if(self.head == None):
            return
        
        if(getPosition == 1):
            self.removeFirst()
        elif(getPosition == self.iCountNode):
            self.removeLast()
        else:
            temp = self.head

            for i in range(1, getPosition - 1, 1):
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

    Obj = SinglyLL()

    Obj.addFirst(10)
    Obj.addFirst(20)
    Obj.addFirst(30)

    Obj.displayLL()

    Obj.addLast(100)
    Obj.addLast(200)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total nodes in LL are: ",iRet)

    Obj.addAtPosition(3, 111)
    Obj.addAtPosition(1, 000)
    Obj.addAtPosition(7, 888)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total nodes in LL are: ",iRet)

    Obj.removeFirst()

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total nodes in LL are: ",iRet)

    Obj.removeLast()
    
    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total nodes in LL are: ",iRet)

    print()

    Obj.removeAtPosition(6)
    Obj.removeAtPosition(1)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total nodes in LL are: ",iRet)

    Obj.clear()
    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total nodes in LL are: ",iRet)

#########################################
if __name__ == "__main__":
    main()