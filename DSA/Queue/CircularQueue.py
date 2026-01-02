# Circular Queue

# node of circular queue
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

# queue class
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count_node = 0
    
    # insert the node
    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = self.rear = new_node
            new_node.next = self.front
            self.count_node += 1
            return True
        
        self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front
        self.count_node += 1
        return True
    
    # remove first node
    def dequeue(self):
        if self.front is None:
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

   # peek from queue
    def peek(self):
        if self.front is None:
            return -1
        return self.front.data

    # check queue is empty or not
    def is_empty(self):
        return self.front is None

    # size of queue
    def size(self):
        return self.count_node

    # display the queue
    def show(self):
        if self.front is None:
            print("Queue is Empty !!")
            return 
        
        temp = self.front
        print("->Front->",end="")
        for _ in range(self.count_node):
            print(f"|{temp.data}|->",end="")
            temp = temp.next
        print("Rear->")

def main():
    queue_obj = Queue()

    queue_obj.enqueue(10)
    queue_obj.enqueue(20)
    queue_obj.enqueue(30)

    queue_obj.show()

    # queue_obj.dequeue()

    ret = queue_obj.peek()
    print(ret)

    ret = queue_obj.is_empty()
    print(ret)

if __name__ == "__main__":
    main()
        
