# <------------------------------ STACK ---------------------------->

# user defined Exception for stack under flow
class StackUnderflowError(Exception):
    # Raised when an invalid operation is performed on an empty stack.
    pass

# node for stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class
class Stack:
    def __init__(self):
        self.top = None
        self.count_node = 0
    
    def push(self, data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
            self.count_node += 1
            return True
        
        new_node.next = self.top
        self.top = new_node

        self.count_node += 1
        return True
    
    def pop(self):
        if self.top is None: # stack underflow
            raise StackUnderflowError("Stack underflow: cannot pop element from stack.")
            
        value = self.top.data
        self.top = self.top.next
        self.count_node -= 1
        return value    
    
    def peek(self):
        if self.top is None: # stack underflow
            raise StackUnderflowError("Stack underflow: cannot peek/top element from stack.")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def show(self):
        if self.top is None:
            print("Stack is empty")
            return
        
        temp = self.top
        while temp != None:
            print(f"|{temp.data}|")
            temp = temp.next
    
    def size(self):
        return self.count_node

    def count(self, value):
        if self.top is None:
            raise StackUnderflowError("Stack is underflow : cannot count value")
        total_count = 0
        temp = self.top
        while temp != None:
            if value == temp.data:
                total_count += 1
            temp = temp.next
        return total_count

def main():
    stack_obj = Stack()

    border = '-'*50
    user_choice, data, ret = 0, None, False

    while True:
        try:
            print(border)
            print('''0. close the program
1. push element 
2. pop element
3. peek/top element
4. check stack is empty or not 
5. show the stack
6. get the size of stack
7. count the value of stack''')
            print(border)

            user_choice = int(input("Enter your choice: "))

            print(border)

            if user_choice == 0:
                print("Program is closed..")
                break
            elif user_choice == 1:
                data = input("Enter your data: ")
                ret = stack_obj.push(data)
                print("Data pushed succesfully." if ret else "Unable to push data into stack!")
                
            elif user_choice == 2:
                print(f"Popped element is: {stack_obj.pop()}")

            elif user_choice == 3:
                print(f"Top element of stack is: {stack_obj.peek()}")

            elif user_choice == 4:
                print("stack is empty" if stack_obj.is_empty() else "Stack is not empty")
                
            elif user_choice == 5:
                stack_obj.show()
                
            elif user_choice == 6:
                print(f"Size of stack is '{stack_obj.size()}'")

            elif user_choice == 7:
                data = input("Enter your data: ")
                print(f"value {data} occurred '{stack_obj.count(data)}' times")

            else:
                print("you entered wrong choice!")
                continue

        except StackUnderflowError as e1:
                print("ERROR",e1)
        except Exception as e:
                print("ERROR, Unexpected Exception Occured", e)

if __name__ == "__main__":
    main()