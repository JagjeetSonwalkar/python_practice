import math

class Number:
    # Find all factors of a number
    def all_fact(self, num):
        fact = []
        for i in range(1,num):
            if num % i == 0:
                fact.append(i)
        return fact
    
    # Count number of factors
    def count_fact(self, num):
        count = 0
        for i in range(1,num):
            if num % i == 0:
                count += 1
        return count
    
    # Find factorial of a number
    def factorial(self, num):
        fact = 1
        for i in range(1, num):
            if i % num == 0:
                fact *= i
        return fact

def main():
    obj = Number()
    ret = None

    num = 6

    ret = obj.all_fact(num)
    print(f"All factors of a number: {num} is: {ret}")

    ret = obj.count_fact(num)
    print(f"All factors of a number: {num} is: {ret}")

    ret = obj.factorial(num)
    print(f"The factoial of number: {num} is: {ret}")

    print(f"The factoial of number: {num} is: {math.factorial(num)}")

if __name__ == "__main__":
    main()