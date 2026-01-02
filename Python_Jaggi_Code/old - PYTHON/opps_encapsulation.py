# Encapsulation
class Math:
    def __init__(self):
        self.__result = 0
    
    def add(self , a, b):
        self.__result = a + b
        return self.__result
    
    def sub(self,a, b):
        self.__result = a - b
        return self.__result

    def mul(self, a, b):
        self.__result = a * b
        return self.__result

    def get_result(self):
        return self.__result

    def __del__(self):
        self.__result = 0

def main():
    ret = None
   
    math_obj = Math()

    ret = math_obj.add(20,10)
    print(f"Addition is {ret}")

    ret = math_obj.sub(20,5)
    print(f"Subtraction is {ret}")

if __name__ == "__main__":
    main()