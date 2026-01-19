# <--------------------------- Singly Linked List -------------------------------------->

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count_node = 0
        
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count_node += 1
        return True

    def size(self):
        return self.count_node

    def display(self):
        if self.head is None:
            return False
        temp = self.head
        while temp is not None:
            print(f"|{temp.data}|->",end="")
            temp = temp.next
        print("NULL")
        return True

    # <-- SORT -->
    def sort(self, desc = False):
        if self.head is None or self.head.next is None:
            return False
        
        f_node = self.head
        while f_node is not None:
            min_node = f_node
            s_node = f_node.next

            while s_node is not None:
                if desc == True:
                    if s_node.data > min_node.data:
                        min_node = s_node
                    s_node = s_node.next

                elif desc == False:
                    if s_node.data < min_node.data:
                        min_node = s_node
                    s_node = s_node.next
            
            f_node.data, min_node.data = min_node.data, f_node.data
            f_node = f_node.next

def main():
    ll = SinglyLinkedList()

    ll.insert(10)
    ll.insert(20)
    ll.insert(15)
    ll.insert(25)
    ll.insert(5)
    ll.insert(3)

    ll.display()

    print("LL sort: ")
    ll.sort()
    ll.display()

    ll.sort(True)
    ll.display()

    
if __name__ == "__main__":
    main()