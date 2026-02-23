# Access Private Attribute via Getter Method
# Implement Method to Update Private Attribute via Setter

class Student:
    def __init__(self,id, name, age):
        # instance attributes
        self.__id = id      # private
        self.name = name    # public
        self.__age = age    # private

    # getter
    def get_age(self):
        return self.__age

    # setter
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age !")

def main():

    student1_obj = Student(101, "rocky das", 50)

    # print("id of student:",student1_obj.__id)     # ERROR # Not work
    print("id of student:",student1_obj.get_age())

    student1_obj.set_age(25)
    print("id of student:",student1_obj.get_age())

if __name__ == "__main__":
    main()