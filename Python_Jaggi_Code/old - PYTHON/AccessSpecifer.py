class Student:
    #constructor
    def __init__(self, A, B, C):
        self.name = A;    #public
        self._Age = B;    #protected
        self.__marks = C; #private

    def display(self):
        print(self.name)
        print(self._Age)
        print(self.__marks)

Obj = Student("Rahul",19,99)
Obj.display();

print(Obj.name);
print(Obj._Age);
# print(Obj.__marks);