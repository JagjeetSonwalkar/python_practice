# Queue

# Node for queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class
class Queue:
    def __init__(self):
        self.front = None
        self.count_node = 0
    
    # add element in last 
    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.count_node += 1
            return True
        
        temp = self.front
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

        self.count_node += 1
        return True
    
    # remove element from first
    def dequeue(self):
        if self.front is None:
            return False
        
        dequeue_node = self.front
        self.front = self.front.next

        dequeue_node.next = None
        self.count_node -= 1
        return True
    
    # get front data
    def peek(self):
        if self.front is None:
            return -1
        return self.front.data
    
    # checck the queue is empty or not
    def is_empty(self):
        return self.front is None
        
    # get size of queue
    def size(self):
        return self.count_node
    
    # display the Queue
    def show(self):
        if self.front is None:
            print("Queue is empty!!")
            return
        
        temp = self.front
        print("FRONT->",end="")
        while temp is not None:
            print(f"|{temp.data}|->",end="")
            temp = temp.next
        print("None",end="")
        print()
      
def main():
    queue_obj = Queue()

    choice, data, value = None, None, None

    while True:
        print("\n--- QUEUE MENU ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Is Empty")
        print("5. Size")
        print("6. Display")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting queue shell...")
            break

        elif choice == "1":
            data = int(input("Enter data: "))
            queue_obj.enqueue(data)
            print("Element inserted")

        elif choice == "2":
            ret = queue_obj.dequeue()
            if ret:
                print("Element removed")
            else:
                print("Queue is empty")

        elif choice == "3":
            value = queue_obj.peek()
            if value == -1:
                print("Queue is empty")
            else:
                print("Front element:", value)

        elif choice == "4":
            print("Queue is empty" if queue_obj.is_empty() else "Queue is not empty")

        elif choice == "5":
            print("Queue size:", queue_obj.size())

        elif choice == "6":
            queue_obj.show()

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()