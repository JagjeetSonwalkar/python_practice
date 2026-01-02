# Create a Class and Print Object Attributes
class Car:
    def __init__(self, brand, model):
        # attributes
        self.brand = brand
        self.model = model

# Add Method to Class to Display Message
class Message:
    def greeting(self):
        return "Hello"
    def bye(self):
        return "Good bye"

# Initialize Object Using Constructor
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def display_object(self):
        print(f"Brand: {self.brand}, RAM: {self.ram} GB")

# Create Method to Return Sum of Two Numbers
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sum(self):
        return self.a + self.b


def main():
    ret = None

    car_object = Car("Toyota", "Corolla")
    print(f"The car brand name is {car_object.brand} & model is {car_object.model}")

    message_obj = Message()
    print(message_obj.greeting())

    dell_obj = Laptop("Dell", 16)
    dell_obj.display_object()

    calculate = Math(10,5)
    ret = calculate.sum()
    print(f"Addition of 2 number is {ret}")

    
    

if __name__ == "__main__":
    main()