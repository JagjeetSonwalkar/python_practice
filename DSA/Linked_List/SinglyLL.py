# <--------------------------- Singly Linked List -------------------------------------->

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count_node = 0
        
    # insert the node at first
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count_node += 1
        return True

    # append the node at last
    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        self.count_node += 1
        return True

    # insert at the given index
    def insert_at(self, data, index):
        if index < 0 or index > self.count_node:
            return False
        elif index == 0:
            return self.insert(data)
        elif index == self.count_node:
            return self.insert_last(data)
        else:
            new_node = Node(data)

            temp = self.head

            for i in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

            self.count_node += 1
            return True

    # del first node
    def remove(self):
        if self.head is None:
            return False

        first_node = self.head
        self.head = self.head.next
        first_node.next = None

        self.count_node -= 1
        return True

    # delete last node
    def remove_last(self):
        if self.head is None:
            return False

        if self.head.next is None:
            self.head = None
            self.count_node -= 1
            return True

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        last_node = temp.next
        temp.next = None
        last_node.next = None

        self.count_node -= 1
        return True

    # delete at given index
    def remove_at(self, index):
        if index < 0 or index >= self.count_node:
            return False

        if index == 0:
            return self.remove()

        if index == self.count_node - 1:
            return self.remove_last()

        temp = self.head
        for i in range(index-1):
            temp = temp.next

        del_node = temp.next
        temp.next = del_node.next
        del_node.next = None
        self.count_node -= 1
        return True

    # delete by value
    def remove_by_value(self, value):
        if self.head is None:
            return False

        if self.head.data == value:
            return self.remove()

        current_node = self.head.next
        previous_node = self.head
        while current_node is not None:
            if current_node.data == value:
                previous_node.next = current_node.next
                current_node.next = None
                self.count_node -= 1
                return True
            previous_node = current_node
            current_node = current_node.next
        return False

    # clear LL
    def clear(self):
        if self.head is None:
            return False

        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = None
            self.count_node -= 1
            current_node = next_node
        self.head = None
        return True

    # get index of value
    def get_index(self, value):
        if self.head is None:
            return -1

        index = 0
        current_node = self.head
        while current_node is not None:
            if current_node.data == value:
                return index
            index += 1
            current_node = current_node.next
        return -1

    # search value exists or not
    def is_exist(self, data):
        if self.head is None:
            return False
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    # check the ll is empty or not
    def is_empty(self):
        if self.head is None:
            return True
        return False

    # check count of occurrence element
    def count(self, element):
        if self.head is None:
            return 0

        current_node = self.head
        total_count = 0
        while current_node is not None:
            if current_node.data == element:
                total_count += 1
            current_node = current_node.next
        return total_count

    # return size of LL
    def size(self):
        return self.count_node

    # display the whole LL
    def display(self):
        if self.head is None:
            return False
        temp = self.head
        while temp is not None:
            print(f"|{temp.data}|->",end="")
            temp = temp.next
        print("NULL")
        return True
def main():
    # variable used for main()
    choice, index, data, ret, border = 0, 0, None, False, '-' * 69

    # object/variable of LinkedList class
    linked_list_obj = SinglyLinkedList()
    
    while True:
        print(border)
        print("""note index start from 0 to n
0. close the program
1. insert the node at beginning
2. insert the node at end
3. insert the node at given index
4. remove the node at beginning
5. remove the node at end
6. remove the node at given index
7. remove the node by value
8. clear the linked list
9. get the index of given value
10. check the value exists or not
11. check the linked list is empty or not
12. count the occurrence of given value
13. get the size of linked list
14. display the linked list""")
        print(border)
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("The program is closed...")
            exit()
        elif choice == 1:
            data = input("Enter the data: ")
            ret = linked_list_obj.insert(data)
            if ret:
                print("Data inserted successfully")
            else:
                print("Data not inserted !!")
        elif choice == 2:
            data = input("Enter the data: ")
            ret = linked_list_obj.insert_last(data)
            if ret:
                print("Data inserted successfully")
            else:
                print("Data not inserted !!")
        elif choice == 3:
            data = input("Enter the data: ")
            index = int(input("Enter the index: "))
            ret = linked_list_obj.insert_at(data, index)
            if ret:
                print(f"Data inserted successfully at index {index}")
            else:
                print(f"Data not inserted!! at index {index}")
        elif choice == 4:
            ret = linked_list_obj.remove()
            if ret:
                print("Data removed successfully")
            else:
                print("Data not removed !!")
        elif choice == 5:
            ret = linked_list_obj.remove_last()
            if ret:
                print("Data removed successfully")
            else:
                print("Data not removed !!")
        elif choice == 6:
            index = int(input("Enter the index: "))
            ret = linked_list_obj.remove_at(index)
            if ret:
                print(f"Data removed successfully from the index {index}")
            else:
                print(f"Data not removed!! from index {index}")
        elif choice == 7:
            data = input("Enter the data: ")
            ret = linked_list_obj.remove_by_value(data)
            if ret:
                print("Data removed successfully")
            else:
                print("Data not removed !!")
        elif choice == 8:
            ret = linked_list_obj.clear()
            if ret:
                print("Data cleared successfully & Now, the Linked List is empty")
            else:
                print("Data not cleared !!")
        elif choice == 9:
            value = input("Enter the value: ")
            ret = linked_list_obj.get_index(value)
            if ret != -1:
                print(f"Data found at index {ret}")
            else:
                print("Data not found !!")
        elif choice == 10:
            value = input("Enter the value to check it exists or not: ")
            ret = linked_list_obj.is_exist(value)
            if ret:
                print("Data found successfully")
            else:
                print("Data not found !!")
        elif choice == 11:
            ret = linked_list_obj.is_empty()
            if ret:
                print("Linked List is empty")
            else:
                print("Linked List is not empty")
        elif choice == 12:
            data = input("Enter the data: ")
            ret = linked_list_obj.count(data)
            if ret == 0:
                print(f"Data not exists!!")
            else:
                print(f"Data Occurred '{ret}' times")
        elif choice == 13:
            ret = linked_list_obj.size()
            print(f"Linked List size is {ret}")
        elif choice == 14:
            ret = linked_list_obj.display()
            if not ret:
                print("Linked List is empty")
        else:
            print("Invalid choice")
    
if __name__ == "__main__":
    main()