# Priority Queue: Lower value ⇒ Higher priority (Ascending Priority Queue)

# node of priority queue
class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

# Priority Queue class   
class PriorityQueue:
    def __init__(self):
        self.front = None
        self.count_node = 0

    # Insert element based on priority
    def enqueue(self, data, priority):
        new_node = Node(data, priority)

        # Case 1: Empty queue or highest priority
        if self.front is None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            self.count_node += 1
            return True

        # Case 2: Find correct position
        temp = self.front
        while temp.next and temp.next.priority <= priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        self.count_node += 1
        return True
    
    # Remove highest priority element
    def dequeue(self):
        if self.front is None:
            return False

        del_node = self.front
        self.front = self.front.next
        del_node.next = None
        self.count_node -= 1
        return True

    # Peek highest priority element
    def peek(self):
        if self.front is None:
            return -1
        return (self.front.data, self.front.priority)
    
    # Check empty
    def is_empty(self):
        return self.front is None

    # Size
    def size(self):
        return self.count_node

    # Display queue
    def show(self):
        if self.front is None:
            print("Priority Queue is Empty")
            return

        temp = self.front
        print("Front -> ", end="")
        while temp:
            print(f"|{temp.data}, P={temp.priority}| -> ", end="")
            temp = temp.next
        print()

# ----------------------------------
# Entry point function
# ----------------------------------
def main():
    pq_obj = PriorityQueue()
    border = "-" * 70

    while True:
        print(border)
        print("""0. Exit
1. Insert element
2. Remove highest priority element
3. Peek highest priority element
4. Check if queue is empty
5. Get size of queue
6. Display priority queue""")
        print(border)

        user_choice = int(input("Enter your choice: "))
        print(border)

        if user_choice == 0:
            print("Priority Queue shell closed.")
            break

        elif user_choice == 1:
            data = input("Enter data: ")
            priority = int(input("Enter priority (int): "))
            ret = pq_obj.enqueue(data, priority)
            print("Data inserted successfully." if ret else "Insertion failed.")

        elif user_choice == 2:
            ret = pq_obj.dequeue()
            print("Element removed successfully." if ret else "Queue is empty.")

        elif user_choice == 3:
            ret = pq_obj.peek()
            if ret != -1:
                print(f"Front Element: {ret[0]}, Priority: {ret[1]}")
            else:
                print("Queue is empty.")

        elif user_choice == 4:
            print("Queue is empty." if pq_obj.is_empty() else "Queue is NOT empty.")

        elif user_choice == 5:
            print("Size of Priority Queue:", pq_obj.size())

        elif user_choice == 6:
            pq_obj.show()

        else:
            print("Invalid choice!")


# ----------------------------------
# Call main
# ----------------------------------
if __name__ == "__main__":
    main()
    