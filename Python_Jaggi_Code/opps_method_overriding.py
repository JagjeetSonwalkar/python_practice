# Run-Time Polymorphism : Method Overriding

class Base:
    def __init__(self):
        self.a = 0
        print("Inside base constructor.")

    def fun(self):
        print("inside base fun")

    def gun(self):
        print("Inside Base gun")

    def sun(self):
        print("inside base sun")
    
    def run(self):
        print("inside base run")

class Derived(Base):
    def __init__(self):
        self.x = 0
        print("inside derived constructor")
    
    def fun(self):
        print("inside derived fun")

    def sun(self):
        print("inside derived sun")

    def mun(self):
        print("inside derived mun")

    def bun(self):
        print("inside derived bun")
    
def main():
    obj = Base()

    obj.fun()
    obj.gun()
    obj.sun()
    obj.run()
    obj.mun()
    obj.bun()

if __name__ == "__main__":
    main()