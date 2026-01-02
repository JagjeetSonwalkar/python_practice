
class Node:
    def __init__(self, A):
        self.data = A 
        self.next = None
        self.prev = None

class DCLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.iCountNode = 0

    def countNode(self):
        return self.iCountNode

    def displayLL(self):
        if self.head is None:
            return "List is empty"

        temp = self.head

        while True:
            print("<=>",temp.data,end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("<=>")

    def addFirst(self, getData):
        newn = Node(getData)

        if((self.head == None) and (self.tail == None)):
            self.head = newn
            self.tail = newn
        else:
            newn.next = self.head
            self.head = newn

        self.tail.next = self.head
        self.head.prev = self.tail

        self.iCountNode = self.iCountNode + 1

    def addLast(self, getData):
        newn = Node(getData)

        if((self.head is None) and (self.tail is None)):
            self.head = newn
            self.tail = newn
            newn.next = self.head
            newn.prev = self.tail
        else:
            newn.prev = self.tail
            newn.next = self.head
            self.tail.next = newn
            self.head.prev = newn
            self.tail = newn

        self.iCountNode = self.iCountNode + 1

    def addAtPosition(self, getPosition, getData):
        
        if(getPosition == 1):
            self.addFirst(getData)
        elif(getPosition == self.iCountNode+1):
            self.addLast(getData)
        else:
            newn = Node(getData)

            temp = self.head

            for i in range(1, getPosition-1, 1):
                temp = temp.next
            newn.next = temp.next 
            newn.prev = temp
            temp.next.prev = newn
            temp.next = newn

            self.iCountNode = self.iCountNode + 1

    def removeFirst(self):

        if(self.head is None and self.tail is None):
            return "List is empty !!"
        
        if(self.head.prev == self.tail.next):
            del head
            del tail
            head = None
            tail = None

            self.iCountNode = self.iCountNode - 1
        else:
            self.head = self.head.next

            self.tail.next = self.head
            self.head.prev = self.tail

            self.iCountNode = self.iCountNode - 1

    def removeLast(self):
        if(self.head is None and self.tail is None):
            return "List is empty !!"
        
        if(self.head.prev == self.tail.next):
            del head
            del tail
            head = None
            tail = None

            self.iCountNode = self.iCountNode - 1
        else:
            self.tail = self.tail.prev

            self.tail.next = self.head
            self.head.prev = self.tail

            self.iCountNode = self.iCountNode - 1

    def removeAtPos(self, getPosition):
        if(self.head is None and self.tail is None):
            return "List is empty !!"

        if(getPosition == 1):
            self.removeFirst()
        elif(getPosition == self.iCountNode):
            self.removeLast()
        else:
            temp = self.head

            for i in range(1, getPosition, 1):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

            self.iCountNode = self.iCountNode - 1

    def clear(self):
        if(self.head is None and self.tail is None):
            return "List is empty !!"

        temp = self.head

        while True:
            temp = temp.next
            nextNode = temp.data
            del nextNode
            self.iCountNode = self.iCountNode - 1
            if temp == self.head:
                break
        
        self.head = None
        self.tail = None

        self.iCountNode = 0

def main():
    iRet = 0
    Obj = DCLL()

    Obj.addFirst(30)
    Obj.addFirst(20)
    Obj.addFirst(10)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.addLast(11)
    Obj.addLast(22)
    Obj.addLast(33)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.addAtPosition(1, 111)
    Obj.addAtPosition(8, 222)
    Obj.addAtPosition(5, 000)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.removeFirst()
    Obj.removeLast()

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.removeAtPos(1)
    Obj.removeAtPos(6)
    Obj.removeAtPos(3)

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    Obj.clear()

    Obj.displayLL()
    iRet = Obj.countNode()
    print("Total Nodes in LL are: ",iRet)

    ##########################################

if __name__ == "__main__":
    main()