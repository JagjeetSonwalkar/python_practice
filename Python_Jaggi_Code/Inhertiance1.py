
class Circle:
    PI = 3.14

    def __init__(self, A):
        self.Raduis = A
    
    def CalculateArea(self):
        iResult = 0.0
        iResult = Circle.PI * (self.Raduis ** 2)
        return iResult
    
def main():
    Obj = Circle(10.5)

    iRet = Obj.CalculateArea()

    print("Area of circle is: ",iRet)

if __name__ == "__main__":
    main()