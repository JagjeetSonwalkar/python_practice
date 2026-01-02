# deque

# node of deque
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# deque class
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count_node = 0
    
    # insert at front
    def enqueue_front(self, data):
        new_node = Node(data)

        if self.front is None and self.rear is None:
            self.front = self.rear = new_node
            new_node.next = self.front
            self.count_node += 1
            return True
        
        new_node.next = self.front
        self.front = new_node
        self.rear.next = new_node
        self.count_node += 1
        return True
    
    # insert at rear
    def enqueue_rear(self, data):
        if self.front is None and self.rear is None:
            return self.enqueue_front(data)

        new_node = Node(data)

        self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front
        self.count_node += 1
        return True
    
    # remove at front
    def dequeue_front(self):
        if self.front is None and self.rear is None:
            return False
        
        if self.front == self.rear:
            self.front = self.rear = None
            self.count_node -= 1
            return True
        
        del_node = self.front

        self.front = self.front.next
        self.rear.next = self.front 

        del_node.next = None
        self.count_node -= 1
        return True
    
    # remove at rear
    def dequeue_rear(self):
        if self.front is None and self.rear is None:
            return False
        
        if self.front == self.rear:
            return self.dequeue_front()
        
        temp = self.front
        for _ in range(self.count_node - 2):
            temp = temp.next
        
        del_node = temp.next
        self.rear = temp
        self.rear.next = self.front

        del_node.next = None
        self.count_node -= 1
        return True

    # peek front 
    def peek_front(self):
        if self.front is None and self.rear is None:
            return -1
        return self.front.data
    
    # peek rear
    def peek_rear(self):
        if self.front is None and self.rear is None:
            return -1
        return self.rear.data
    
    # check deque is empty or not
    def is_empty(self):
        return self.front is None
           
    # get size of deque
    def size(self):
        return self.count_node

    # display deque
    def show(self):
        if self.front is None and self.rear is None:
            print("deque is Empty")
            return
        
        temp = self.front
        print("Front",end="")
        for _ in range(self.count_node):
            print(f"<=|{temp.data}|=>",end="")
            temp = temp.next
        print("Rear",end="")
        print()

# ----------------------------------
# entry point function: main
# ----------------------------------
def main():
    queu_obj = Deque()

    border = '-' * 69
    user_choice, ret, data = 0, False, None

    while True:
        print(border)
        print("""0. exit the deque shell
1. insert at front
2. insert at rear
3. remove from front
4. remove from rear
5. peek from front
6. peek from rear
7. check deque is empty or not
8. get the size of deque
9. display deque""")
        print(border)
        user_choice = int(input("Enter the choice: "))
        print(border)

        if user_choice == 0:
            print("shell of Deque is closed.")
            break

        elif user_choice == 1:
            data = input("Enter the data: ")
            ret = queu_obj.enqueue_front(data)
            print("Data inserted successfully." if ret else "Unable to insert the data !")
            
        elif user_choice == 2:
            data = input("Enter the data: ")
            ret = queu_obj.enqueue_rear(data)
            print("Data inserted successfully." if ret else "Unable to insert the data !")

        elif user_choice == 3:
            ret = queu_obj.dequeue_front()
            print("Data deleted successfully." if ret else "Unable to delete the data !")

        elif user_choice == 4:
            ret = queu_obj.dequeue_rear()
            print("Data deleted successfully." if ret else "Unable to delete the data !")

        elif user_choice == 5:
            ret = queu_obj.peek_front()
            print(f"front element is {ret}" if ret != -1 else "queue is empty!")

        elif user_choice == 6:
            ret = ret = queu_obj.peek_rear()
            print(f"rear element is {ret}" if ret != -1 else "queue is empty!")

        elif user_choice == 7:
            ret = queu_obj.is_empty()
            print("Deque is empty." if ret else "Deque is NOT empty")
        
        elif user_choice == 8:
            ret = queu_obj.size()
            print("size of Deque:",ret)

        elif user_choice == 9:
            queu_obj.show()

        else:
            print("invalid choice !")
# End of main ------------------------------------------------------------------------------>

# ----------------------------------
# call the main function
# ----------------------------------
if __name__ == "__main__":
    main()
