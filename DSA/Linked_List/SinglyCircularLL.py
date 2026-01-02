# <--------------------------------- Singly Circular Linked List -------------------------------------->

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count_node = 0

    # insert the node at beginning
    def insert(self, data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head

            self.count_node += 1
            return True

        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head

        self.count_node += 1
        return True

    # insert the node at last
    def insert_last(self, data):
        new_node = Node(data)

        if self.head is None and self.tail is None:
            return self.insert(data)

        self.tail.next = new_node
        new_node.next = self.head
        self.tail = new_node
        self.count_node += 1
        return True

    # insert the node at given pos
    def insert_at(self, data, index):
        if index < 0 or index > self.count_node:
            return False

        if index == 0:
            return self.insert(data)

        if index == self.count_node:
            return self.insert_last(data)

        new_node = Node(data)

        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.count_node += 1
        return True

    # remove the 1st node
    def remove(self):
        if self.head is None and self.tail is None:
            return False

        if self.head.next == self.head:
            self.head = None
            self.tail = None
            self.count_node -= 1
            return True

        first_node = self.head
        self.head = self.head.next
        self.tail.next = self.head
        first_node.next = None
        self.count_node -= 1
        return True

    # remove the last node
    def remove_last(self):
        if self.head is None and self.tail is None:
            return False

        if self.head.next == self.head:
            return self.remove()

        current_node = self.head

        while current_node.next != self.tail:
            current_node = current_node.next

        last_node = self.tail
        self.tail = current_node
        self.tail.next = self.head

        last_node.next = None
        self.count_node -= 1
        return True

    # remove the node by index
    def remove_at(self, index):
        if index < 0 or index >= self.count_node:
            return False

        if index == 0:
            return self.remove()

        if index == self.count_node - 1:
            return self.remove_last()

        current_node = self.head

        for _ in range(index - 1):
            current_node = current_node.next
        del_node = current_node.next
        current_node.next = del_node.next
        del_node.next = None
        self.count_node -= 1
        return True

    # remove the node if given value exists
    def remove_by_value(self, del_value):
        if self.head is None and self.tail is None:
            return False

        if self.head.data == del_value:
            return self.remove()

        if self.tail.data == del_value:
            return self.remove_last()

        prev_node = self.head
        current_node = self.head.next

        while current_node != self.head:
            if current_node.data == del_value:
                del_node = current_node
                prev_node.next = del_node.next
                del_node.next = None
                self.count_node -= 1
                return True

            prev_node = current_node
            current_node = current_node.next
        return False

    # clear Linked List and make the Linked List empty
    def clear(self):
        if self.head is None and self.tail is None:
            return False

        self.tail.next = None

        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = None
            current_node = next_node
            self.count_node -= 1
        self.head = None
        self.tail = None
        return True

    # size of LL
    def size(self):
        return self.count_node

    # display the whole LL
    def display(self):
        if self.head is None:
            return False

        current_node = self.head

        while True:
            print(f"|{current_node.data}|->",end="")
            current_node = current_node.next
            if current_node == self.head:
                break
        print("[points to first Node]",end=" ")
        return True

def main():
    pass

if __name__ == "__main__":
    main()

