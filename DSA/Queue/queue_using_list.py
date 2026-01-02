# Queue using list

# Queue class
class Queue:
    def __init__(self, capacity = None):
        self.queue = list()
        self.capacity = capacity
    
    # add element in last 
    def enqueue(self, data):
        self.queue.append(data)
        return True
        
    # remove element from first
    def dequeue(self):
        if len(self.queue) == 0:
            return False
        self.queue.remove()
        return True
    
    # get front data
    def peek(self):
        if len(self.queue) == 0:
            return -1
        return self.queue[0]
    
    # checck the queue is empty or not
    def is_empty(self):
        return self.queue == 0
        
    # get size of queue
    def size(self):
        return len(self.queue)
    
    # display the Queue
    def show(self):
        if len(self.queue) == 0:
            print("Queue is empty!")
            return 
        
        print("FRONT->",end="")
        for item in self.queue:
            print(f"|{item}|->",end="")
        print("None",end="")
        print()
      
def main():
    queue_obj = Queue(capacity=5)

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

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting queue shell...")
            break

        elif choice == 1:
            data = input("Enter data: ")
            queue_obj.enqueue(data)
            print("Element inserted")

        elif choice == 2:
            ret = queue_obj.dequeue()
            if ret:
                print("Element removed")
            else:
                print("Queue is empty")

        elif choice == 3:
            value = queue_obj.peek()
            if value == -1:
                print("Queue is empty")
            else:
                print("Front element:", value)

        elif choice == 4:
            print("Queue is empty" if queue_obj.is_empty() else "Queue is not empty")

        elif choice == 5:
            print("Queue size:", queue_obj.size())

        elif choice == 6:
            queue_obj.show()

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()