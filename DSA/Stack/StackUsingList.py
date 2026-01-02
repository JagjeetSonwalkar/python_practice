# <------------------------------ STACK ---------------------------->

# user defined Exception for stack under flow
class StackUnderflowError(Exception):
    # Raised when an invalid operation is performed on an empty stack.
    pass

# user defined Exception for stack over flow
class StackOverflowError(Exception):
    # Raised when an invalid operation is performed on a full stack.
    pass

# Stack class
class Stack:
    def __init__(self, capacity=None):
        self.stack = []
        self.capacity = capacity

    def push(self, data):
        if self.capacity is not None and len(self.stack) >= self.capacity:
            raise StackOverflowError("Stack overflow: capacity reached")
        self.stack.append(data)
        return True

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError("Stack underflow: cannot pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise StackUnderflowError("Stack underflow: cannot peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def show(self):
        print("TOP")
        for item in reversed(self.stack):
            print(f"| {item} |")
        print("BOTTOM")

    def count(self, value):
        if self.is_empty():
            raise StackUnderflowError("Stack underflow: cannot count value")
        return self.stack.count(value)

    def clear(self):
        self.stack.clear()

def main():
    stack_obj = Stack(capacity=5)

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
7. count the value of stack
8. clear stack''')
            print(border)

            user_choice = int(input("Enter your choice: "))
            print(border)

            if user_choice == 0:
                print("Program is closed.")
                break

            elif user_choice == 1:
                data = input("Enter your data: ")
                ret = stack_obj.push(data)
                print("Data pushed successfully." if ret else "Data not pushed")

            elif user_choice == 2:
                print(f"Popped element is: {stack_obj.pop()}")

            elif user_choice == 3:
                print(f"Top element of stack is: {stack_obj.peek()}")

            elif user_choice == 4:
                print("Stack is empty" if stack_obj.is_empty() else "Stack is not empty")

            elif user_choice == 5:
                stack_obj.show()

            elif user_choice == 6:
                print(f"Size of stack is: {stack_obj.size()}")

            elif user_choice == 7:
                data = input("Enter your data: ")
                print(f"Value {data} occurred {stack_obj.count(data)} times")

            elif user_choice == 8:
                stack_obj.clear()
                print("Stack cleared successfully.")

            else:
                print("Invalid choice.")

        except StackUnderflowError as e:
            print("ERROR:", e)
        except StackOverflowError as e:
            print("ERROR:", e)
        except Exception as e:
            print("ERROR: Unexpected exception occurred:", e)


if __name__ == "__main__":
    main()