# <------------------ Doubly Linked List ------------------------------>

# Node of Doubly Linked List
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

# Doubly Linked List class
class DoublyLL:

    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.count_node = 0

    # Insert at beginning
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.count_node += 1
        return True

    # Insert at last
    def insert_last(self, data):
        if self.head is None:
            return self.insert(data)

        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

        self.count_node += 1
        return True

    # Insert at given index
    def insert_at_index(self, data, index):
        if index < 0 or index > self.count_node:
            return False

        if index == 0:
            return self.insert(data)
        if index == self.count_node:
            return self.insert_last(data)

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        next_node = current.next

        new_node.prev = current
        new_node.next = next_node
        current.next = new_node
        next_node.prev = new_node

        self.count_node += 1
        return True

    # Remove first node
    def remove(self):
        if self.head is None:
            return False

        if self.head.next is None:
            self.head = self.tail = None
        else:
            first_node = self.head
            self.head = self.head.next
            self.head.prev = None
            first_node.next = None

        self.count_node -= 1
        return True

    # Remove last node
    def remove_last(self):
        if self.head is None:
            return False

        if self.head.next is None:
            return self.remove()

        last = self.tail
        self.tail = last.prev
        self.tail.next = None
        last.prev = None

        self.count_node -= 1
        return True

    # Remove by index
    def remove_by_index(self, index):
        if self.head is None or index < 0 or index >= self.count_node:
            return False

        if index == 0:
            return self.remove()
        if index == self.count_node - 1:
            return self.remove_last()

        current = self.head
        for _ in range(index):
            current = current.next

        prev_node = current.prev
        next_node = current.next
        prev_node.next = next_node
        next_node.prev = prev_node

        current.next = current.prev = None
        self.count_node -= 1
        return True

    # Remove by value
    def remove_by_value(self, del_value):
        if self.head is None:
            return False

        current = self.head
        while current is not None:
            if current.data == del_value:
                if current == self.head:
                    return self.remove()
                elif current == self.tail:
                    return self.remove_last()
                else:
                    prev_node = current.prev
                    next_node = current.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    current.next = current.prev = None
                    self.count_node -= 1
                    return True
            current = current.next
        return False

    # Clear the entire list
    def clear(self):
        current = self.head
        while current is not None:
            next_node = current.next
            current.prev = current.next = None
            current = next_node
            self.count_node -= 1

        self.head = self.tail = None
        return True

    # Get size
    def size(self):
        return self.count_node

    # Display normal
    def display(self):
        if self.head is None:
            print("List is empty")
            return False

        current = self.head
        print("NULL<=>", end="")
        while current is not None:
            print(f"|{current.data}|<=>", end="")
            current = current.next
        print("NULL")
        return True

def main():
    doubly_ll = DoublyLL()

    # Insert nodes
    doubly_ll.insert(1)
    doubly_ll.insert(2)
    doubly_ll.insert_last(2)
    doubly_ll.insert_last(3)
    doubly_ll.insert_at_index(12, 0)
    doubly_ll.insert_at_index(125, 1)

    doubly_ll.display()

    doubly_ll.display_with_address()


if __name__ == '__main__':
    main()
