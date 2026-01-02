class Employee:
    companyName = "Jaggi";

    def __init__(self, A, B, C):
        print("Inside constructor");
        self.name = A;
        self.salary = B;
        self.city = C;

    def __del__(self):
        print("Inside Desctructor");
        
def main():
    print("class varibale: "+Employee.companyName)

    emp1 = Employee("Rahul",15000,"pune");
    emp2 = Employee("Raju",1000,"Mumbai");

    print(emp1.name);
    print(emp1.salary);
    print(emp1.city);

if __name__ == "__main__":
    main()