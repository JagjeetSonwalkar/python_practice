# Update Attribute of Object
class Student:
    school_name = "Small Talk School"   # class attribute

    def __init__(self,id, name, age):
        # instance attributes
        self.id = id    
        self.name = name
        self.age = age
    
    def display(self):
        print(f"school name: {Student.school_name}")
        print(f"student id: {self.id}, student name: {self.name}, student age: {self.age}")
        print()

    def update_info(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

def main():

    student1_obj = Student(1053, "rocky das", 50)
    student1_obj.display()

    # update the info using method: update_info
    student1_obj.update_info(1001, "rocky das", 51)
    student1_obj.display()

    # update using inbilt_function
    setattr(student1_obj, "name", "Rocky Dass")
    setattr(student1_obj, "id", 1069)
    student1_obj.display()

if __name__ == "__main__":
    main()