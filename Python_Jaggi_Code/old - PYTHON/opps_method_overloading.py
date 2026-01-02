# method overloading (NA)

# this type of method overloading is not allowed in python 
class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def result(self, total_marks, total_subject):
        return (total_marks/total_subject) * 100
    
    def result(self, grade):
        if grade >= 35:
            return True
        return False
    
# so to achieve method overloading we can use: default argument, varibale lenght Argument ,to Behaves like overloaded function

def show(*args):
    for i in args:
        print(i,end=" ")
    print()

show(10)
show(10, 20)
show(10, 20 , 30)