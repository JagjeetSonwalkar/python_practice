'''
STACK is LIFO (Last in, first out)

push: add new element
pop: remove exisiting element
peek: return the top(last) element on the stack
isEmpty: check the stack is empty or not
size: return the number of elements in the stack
'''

class Node:
    def __init__(self, A):
        self.data = A 
        self.next = None

class Stack:
    # constructor
    def __init__(self):
        self.head = None
        self.iCountNode = 0
    
    # push
    def push(self, getData):
        newn = Node(getData)

        if(self.head == None):
            self.head = newn
        else:
            temp = self.head

            while(temp.next != None):
                temp = temp.next
            temp.next = newn
        
        self.iCountNode = self.iCountNode + 1
        return True
    
    # pop
    def pop(self):
        if(self.head == None):
            return False

        returnData = -1
        temp = self.head

        returnData = self.head.data
        self.head = self.head.next

        self.iCountNode = self.iCountNode - 1
        return returnData

    # peek
    def peek(self):
        if(self.head == None):
            return False

        top = None

        top = self.head.data
        return top

    # isEmpty
    def isEmpty(self):
        if(self.head == None):
            return True
        elif(self.head != None):
            return False

    # display the stack
    def show(self):
        if(self.head == None):
            return "Stack is empty !!"

        temp = self.head

        while(temp != None):
            print("|",temp.data,"|")
            temp = temp.next
        print()

    # size
    def size(self):
        if(self.head == None):
            return False

        return self.iCountNode

def main():
    
    # varibale
    Obj = Stack()
    iOption = 0
    iRet = 0
    Data = None

    while True:
        print("||||||||||||||||||||||||||||||||||||||||||||")
        print("0. Terminate the stack.")
        print("1. push or Add new element inside the stack.")
        print("2. pop or delete the existing element.")
        print("3. peek the top element from the stack.")
        print("4. check stack is empty or Not.")
        print("5. total elements in stack")
        print("6. display the stack.")
        print("||||||||||||||||||||||||||||||||||||||||||||")
        iOption = int(input("Enter the option: "))
        print("||||||||||||||||||||||||||||||||||||||||||||")

        if(iOption == 0):
            print("Thnakyou for using the stack.")
            break
        elif(iOption == 1):
            Data = input("Enter the data: ")
            iRet = Obj.push(Data)

            if(iRet == True):
                print("Data inserted succesfully")
            else:
                print("Unable to insert the data !!")
        elif(iOption == 2):
            iRet = Obj.pop()

            if(iRet == False):
                print("stack is empty !!")
            else:
                print("Removed element is: ",iRet)
        elif(iOption == 3):
            iRet = Obj.peek()

            if(iRet == False):
                print("stack is empty !!")
            else:
                print("Top element of stack is: ",iRet)
        elif(iOption == 4):
            iRet = Obj.isEmpty()

            if(iRet == True):
                print("Stack is empty !")
            else:
                print("Stack is NOT empty")
        elif(iOption == 5):
            iRet = Obj.size()

            if(iRet == False):
                print("Stack contain zero elements in it.")
            else:
                print("Stack contain '",iRet,"' elements in it")
        elif(iOption == 6):
            Obj.show()
        else:
            print("Pls, enter a valid option.");
########################################3

if __name__ == "__main__":
    main()