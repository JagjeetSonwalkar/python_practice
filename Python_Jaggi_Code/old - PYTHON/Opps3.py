# Create Object Count Tracker

class Student:
    school_name = "Small Talk School"   # class attribute
    object_count = 0

    def __init__(self,id, name, age):
        # instance attributes
        self.id = id    
        self.name = name
        self.age = age

        Student.object_count += 1

    @classmethod
    def student_count(cls):
        return Student.object_count
    
    def display(self):
        print(f"school name: {Student.school_name}")
        print(f"student id: {self.id}, student name: {self.name}, student age: {self.age}")
        print()

def main():

    student1_obj = Student(101, "rocky das", 50)
    student2_obj = Student(102, "Abhi rocks", 51)
    student3_obj = Student(103, "Rohit sharama", 45)

    student1_obj.display()
    student2_obj.display()
    student3_obj.display()

    print(f"Total student in school are {Student.student_count()}")

if __name__ == "__main__":
    main()