# Print Class Name of an Object
# Check Type of an Object

class Student:
    def __init__(self,id, name, age):
        # instance attributes
        self.__id = id      # private
        self.name = name    # public
        self.__age = age    # private

def main():

    student1_obj = Student(101, "rocky das", 50)

    # Print Class Name of an Object
    class_name = student1_obj.__class__.__name__

    print(f"class name of object: student1_obj is {class_name}")

    # # Check Type of an Object
    print(f"class name of object: student1_obj is {type(student1_obj)}")
    print(f"class name of object: student1_obj is {type(student1_obj).__name__}")
    
    

if __name__ == "__main__":
    main()