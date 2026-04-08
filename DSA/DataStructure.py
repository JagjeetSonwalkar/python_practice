# LL
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.linked_list_size = 0
    
    def insert(self, data):
        new_node = SinglyLinkedListNode(data)

        if self.head == None:
            self.head = new_node
            self.linked_list_size += 1
            return True
        else:
            new_node.next = self.head
            self.head = new_node
            self.linked_list_size += 1
            return True
        return False
    
    def insert_last(self, data):
        if self.head == None:
            return self.insert(data)
        else:
            new_node = SinglyLinkedListNode(data)
            temp = self.head

            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            self.linked_list_size += 1
            return True

        return False

    def insert_at_index(self, index = 0, data = None):
        if index < 0 or index > self.linked_list_size:
            print("ERROR: Index out of range!, Unable to insert node")
            return False

        if self.head == None or index == 0:
            return self.insert(data)
        elif index == self.linked_list_size + 1:
            return self.insert_last(data)
        else:
            new_node = SinglyLinkedListNode(data)
            temp = self.head

            for i in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node 
            self.linked_list_size += 1
            return True
        return False

    def remove(self):
        if self.head is None:
            return False
        if self.head.next is None:
            self.head = None
            self.linked_list_size -= 1
            return True
        else:
            del_node = self.head
            self.head = self.head.next
            del_node.next = None
            del_node = None
            self.linked_list_size -= 1
            return True
        return False

    def remove_last(self):
        if self.head == None:
            return False
        if self.head.next == None:
            return self.remove()
        else:
            temp = self.head

            while temp.next.next != None:
                temp = temp.next
            temp.next = None
            self.linked_list_size -= 1
            return True
        return False

    def remove_at_index(self, index = 0):
        if index < 0 or index > self.linked_list_size:
            print("ERROR: Index out of range!, Unable to insert node")
            return False

        if self.head.next == None or index == 0:
            return self.remove()
        elif index == self.linked_list_size:
            return self.remove_last()
        else:
            temp = self.head

            for _ in range(index - 1):
                temp = temp.next
            del_node = temp.next
            temp.next = temp.next.next
            del_node = None
            self.linked_list_size -= 1
            return True
        return False

    def size(self):
        return self.linked_list_size
    
    def display(self):
        temp = self.head
        for _ in range(0, self.linked_list_size, 1):
            print(temp.data, end = "->")
            temp = temp.next
        print("NULL", end = "")
        print()
        return True
    
    def is_empty(self):
        if self.head == None:
            return True
        return False

def main():
    linked_list = SinglyLinkedList()

    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.insert(40)
    linked_list.insert(50)
    linked_list.insert(60)

    linked_list.insert_last(100)
    linked_list.insert_last(200)

    linked_list.insert_at_index(index=0, data=11)
    linked_list.insert_at_index(index=3, data=55)

    linked_list.display()

    linked_list.remove()
    linked_list.remove_last()
    
    linked_list.display()

    linked_list.remove_at_index(3)

    linked_list.display()

    ret = linked_list.size()
    print("Size of LL is:",ret)

if __name__ == "__main__":
    main()