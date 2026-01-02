
class Demo:
    def addition(self,A, B):
        return A+B
    
class DemoX(Demo):
    def addition(self,A, B, C): # overrided method
        return A+B+C 

Obj = Demo()
Objx = DemoX()

print(Obj.addition(10,20))
print(Objx.addition(10,20,30))