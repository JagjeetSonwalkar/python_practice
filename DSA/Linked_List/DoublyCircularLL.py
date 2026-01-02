# <------------------------ Doubly Circular Linked List --------------------------------->

#------------------------------------------------------
# node for Doubly Circular Linked List
#------------------------------------------------------
class Node:
    def __init__(self, data):
        self.prev = data
        self.data = data
        self.next = data

#------------------------------------------------------
# class of Doubly Circular Linked List for operations
#------------------------------------------------------
class DoublyCircular:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count_node = 0

    #------------------------------------------------------
    # insert the node at beginnig - oth index
    #------------------------------------------------------
    def insert(self, data):
        new_node = Node(data)

        if self.head is None and self.tail is None:
            self.head = self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node

            self.count_node += 1
            return True

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.tail.next = self.head
        new_node.prev = self.tail
        

        self.count_node += 1
        return True

    #------------------------------------------------------
    # insert the node at last
    #------------------------------------------------------
    def insert_last(self, data):
        if self.head is None and self.tail is None:
            return self.insert(data)
        
        new_node = Node(data)

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        new_node.next = self.head
        self.head.prev = self.tail

        self.count_node += 1
        return True

    #------------------------------------------------------
    # insert the node at index
    #------------------------------------------------------
    def insert_by_index(self, data, index):
        if index < 0 or index > self.count_node:
            return False
        
        if index == 0:
            return self.insert(data)
        elif index == self.count_node:
            return self.insert_last(data)
        else:
            new_node = Node(data)

            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            
            temp.next.prev = new_node
            new_node.next = temp.next
            new_node.prev = temp
            temp.next = new_node

            self.count_node += 1
            return True
        
    #------------------------------------------------------
    # remove first node
    #------------------------------------------------------
    def remove(self):
        if self.head is None and self.tail is None:
            return False
        
        if self.count_node == 1:
            self.head.next = self.head = self.tail.next = self.tail = None
            self.count_node -= 1
            return True

        first_node = self.head

        self.head =self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head

        first_node.next = first_node.prev = None
        self.count_node -= 1
        return True

    #------------------------------------------------------   
    # remove last node
    #------------------------------------------------------
    def remove_last(self):
        if self.head is None and self.tail is None:
            return False
        if self.count_node == 1:
            return self.remove()
        
        last_node = self.tail

        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail

        last_node.next = last_node.prev = None
        self.count_node -= 1
        return True

    #------------------------------------------------------
    # remove by index
    #------------------------------------------------------
    def remove_index(self, index):
        if index < 0 or index >= self.count_node:
            return False
        
        if index == 0:
            return self.remove()
        if index == self.count_node - 1:
            return self.remove_last()
        
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        
        del_node = temp.next

        del_node.next.prev = temp
        temp.next = del_node.next

        del_node.next = del_node.prev = None
        self.count_node -= 1
        return True
    
    #------------------------------------------------------
    # remove by value
    #------------------------------------------------------
    def remove_value(self, del_value):
        if self.head is None or self.tail is None:
            return False

        if self.count_node == 1:
            if self.head.data == del_value:
                return self.remove()
            return False

        if self.head.data == del_value:
            return self.remove()
        if self.tail.data == del_value:
            return self.remove_last()
        
        temp = self.head.next
        for _ in range(self.count_node - 2):
            if temp.data == del_value:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

                temp.next = temp.prev = None
                self.count_node -= 1
                return True
            temp = temp.next
        return False

    #------------------------------------------------------
    # clear Linked List
    #------------------------------------------------------
    def clear(self):
        if self.head is None and self.tail is None:
            return False

        self.head.prev = None
        self.tail.next = None
        temp = self.head

        while temp is not None:
            del_node = temp
            temp = temp.next

            del_node.next = del_node.prev = None
            self.count_node -= 1
        
        self.head = None
        self.tail = None
        return True

    #------------------------------------------------------
    # get index of value
    #------------------------------------------------------
    def index(self, value):
        if self.head is None and self.tail is None:
            return -1

        temp = self.head
        for i in range(self.count_node):
            if temp.data == value:
                return i
            temp = temp.next
        
        return -1

    #------------------------------------------------------
    # check linked is empty or not
    #------------------------------------------------------
    def is_empty(self):
        if self.head is None:
            return True
    
    #------------------------------------------------------
    # check value exists or not
    #------------------------------------------------------
    def is_exist(self, value):
        if self.head is None or self.tail is None:
            return False

        if self.head.data == value or self.tail.data == value :
            return True
        
        temp = self.head.next
        for _ in range(self.count_node - 2):
            if temp.data == value:
                return True
            temp = temp.next
        return False

    #------------------------------------------------------
    # display the Doubly Linked List in both order
    #------------------------------------------------------
    def show(self, reverse = False):
        if self.head is None and self.tail is None:
            return False

        if not reverse:
            temp = self.head
            for _ in range(self.count_node):
                print(f"<=|{temp.data}|=>",end="")
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.count_node):
                print(f"<=|{temp.data}|=>",end="")
                temp = temp.prev
        print()
        return True

    #------------------------------------------------------
    # count occurence
    #------------------------------------------------------
    def count(self, value):
        if self.head is None and self.tail is None:
            return 0

        total_count = 0
        temp = self.head
        for _ in range(self.count_node):
            if temp.data == value:
                total_count += 1
            temp = temp.next
        return total_count

    #------------------------------------------------------
    # get size of Linked List
    #------------------------------------------------------
    def size(self):
        return self.count_node

#------------------------------------------------------
# main method
#------------------------------------------------------
def main():
    #------------------------------------------------------
    # varibale used in main method
    #------------------------------------------------------
    border, user_choice, data, ret, index = '-' * 50, 0, None, None, 0
    linked_list = DoublyCircular()

    print("You are using Doubly Linked list".center(25, '-'))
    #------------------------------------------------------
    # shell
    #------------------------------------------------------
    while True:
        print(border)
        print('''0. close the program
1. insert the node at beginning
2. insert the node at end
3. insert the node at given index
4. remove the node at beginning
5. remove the node at end
6. remove the node at given index
7. remove the node by value
8. clear the linked list
9. get the index from given value
10. check the value exists or not
11. check the linked list is empty or not
12. count the occurrence of given value
13. get the size of linked list
14. display the linked list
15. display the linked list in reverse order''')
        print(border)
        user_choice = int(input("Enter you choice:  "))
        print(border)
        if user_choice == 0:
            print("The program is closed...")
            exit()
        elif user_choice == 1:
            data = input("Enter you data: ")
            ret = linked_list.insert(data)
            if ret:
                print("Data inserted successfully")
            else:
                print("Unable to insert the data !")
        elif user_choice == 2:
            data = input("Enter you data: ")
            ret = linked_list.insert_last(data)
            if ret:
                print("Data inserted successfully")
            else:
                print("Unable to insert the data !")
        elif user_choice == 3:
            data = input("Enter the data: ")
            index = int(input("Enter the index: "))
            ret = linked_list.insert_by_index(data, index)
            if ret:
                print(f"Data inserted successfully at index {index}")
            else:
                print(f"Unable t0 inserted data at index {index}!!")
        elif user_choice == 4:
            ret = linked_list.remove()
            if ret:
                print("Data removed successfully")
            else:
                print("Data not removed !!")
        elif user_choice == 5:
            ret = linked_list.remove_last()
            if ret:
                print("Data removed successfully")
            else:
                print("Data not removed !!")
        elif user_choice == 6:
            index = int(input("Enter the index: "))
            ret = linked_list.remove_index(index)
            if ret:
                print(f"Data removed successfully from the index {index}")
            else:
                print(f"Unable to remove the data from index {index} !!")
        elif user_choice == 7:
            data = input("Enter the data: ")
            ret = linked_list.remove_value(data)
            if ret:
                print("Data removed successfully")
            else:
                print("Unable to remove data !!")
        elif user_choice == 8:
            ret = linked_list.clear()
            if ret:
                print("Data cleared successfully & Now, the Linked List is empty")
            else:
                print("Data not cleared !!")
        elif user_choice == 9:
            data = input("Enter the value: ")
            ret = linked_list.index(data)
            if ret != -11:
                print(f"Data found at index {ret}")
            else:
                print("Data not found !!")
                           
        elif user_choice == 10:
            value = input("Enter the value to check it exists or not: ")
            ret = linked_list.is_exist(value)
            if ret:
                print("Data exists")
            else:
                print("Data not exists!!")
        elif user_choice == 11:
            ret = linked_list.is_empty()
            if ret:
                print("Linked List is empty")
            else:
                print("Linked List is not empty")
        elif user_choice == 12:
            data = input("Enter the data to count occurence: ")
            ret = linked_list.count(data)
            print(f"Data Occurred '{ret}' times")
        elif user_choice == 13:
            ret = linked_list.size()
            print(f"size of Linked list: {ret}")
        elif user_choice == 14:
            ret = linked_list.show(reverse=False)
            if not ret:
                print("Unable to display Linked List!")
        elif user_choice == 15:
            ret = linked_list.show(reverse=True)
            if not ret:
                print("Unable to display Linked List!")
        else:
            print("Invalid choice")
            continue
#------------------------------------------------------   
# End of main 
#------------------------------------------------------

if __name__ == "__main__":
    main()