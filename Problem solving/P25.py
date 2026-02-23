# 	Take a name as input and greet the user.
# 	Take a float number and print it.
# 	Take a character and print its ASCII value.
# 	Take two inputs and print in reverse order.

def greet(getName):
    print("Good Morning,",getName,"have a good day.")

def printReverse(getInput1, getInput2):
    revString1 = getInput1[::-1]
    revString2 = str(getInput2)[::-1]
    
    print(revString1,"\t",revString2)
    

def main():
    sName = None
    fPercent = 0.0
    cBloodGroup = None

    sName = input("Enter your name: ")
    greet(sName)

    fPercent = float(input("Enter your percentage: "))
    print("Your percentage is: ",fPercent)

    cBloodGroup = input("Enter your blood group: ")
    cBloodGroup = cBloodGroup[0]
    print("ASCII Value of your character is: ",ord(cBloodGroup))

    printReverse(sName, fPercent)

if __name__ == "__main__":
    main()
