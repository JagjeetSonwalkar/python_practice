def Display():
    print("Welcome to my code! ")

print("This line always run.")
print("Value of __name__is: ",__name__)

if __name__ == "main":
    print("This code runs only when run directly.")
    Display()