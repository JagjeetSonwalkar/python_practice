# Method overloading is not allowed

class Demo:
    def addition(A, B):
        return A+B
    
    def addition(A, B, C):
        return A+B+C 

Obj = Demo()

print(Obj.addition(10,20))
print(Obj.addition(10,20,30))
