
class Circle:
    PI = 3.14

    def __init__(self, A):
        self.Raduis = A
        print("Inside the Circle constructor")
    
    def CalculateArea(self):
        iResult = 0.0
        iResult = Circle.PI * (self.Raduis ** 2) # not use self.PI 
        return iResult

class CircleX(Circle):
    def __init__(self, B):
        # self.Raduis = B
        super().__init__(B)  #it is used to access the Raduis instance variable insted on creating new one
        print("Inside the CircleX constructor")

    def CalculateCircumference(self):
        iResult = 0.0
        iResult = 2 * Circle.PI * self.Raduis
        return iResult
    
def main():
    Obj = CircleX(10.5)

    iRet = Obj.CalculateArea()
    print("Area of circle is: ",iRet)

    iRet = Obj.CalculateCircumference()
    print("Circumference of circle is: ",iRet)

if __name__ == "__main__":
    main()