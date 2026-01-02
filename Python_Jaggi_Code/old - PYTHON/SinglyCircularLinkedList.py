'''
    Linked list is data structure 
    operations on LL: Insertion(At beginning, At end, At a specfic position), Deletion(At beginning, At end, At a specfic position),
    Traversal(Displaying elements, Searching),size of linked list,  Updating(Modification), Merging, Reversal
'''

# Node
class Node:
    def __init__(self, A):
        self.data = A
        self.next = None

# Singly circular LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.iCountNode = 0

    # Insertion - At beginning
    def add(self, getData):
        newn = Node(getData)

        if(self.head == None):
            self.head = newn
            self.tail = newn
        else:
            newn.next = self.head
            self.head = newn
        
        self.tail.next = self.head
        self.iCountNode = self.iCountNode + 1
    
###########################
def main():
    Obj = LinkedList()

    Obj.add(10)
    Obj.add(20)
    Obj.add(30)

    iRet = Obj.size()
    print(iRet)

##########################
if __name__ == "__main__":
    main()