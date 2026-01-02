import math

def main():
    a = 10.65
    x = 99
    z = -5

    result = None

    result = round(a)
    print(f"result of decimal using round function: {result}")

    result = abs(z)
    print(f"result of -ve value using abs function: {result}")

    result = math.sqrt(a)
    print(f"square root of {a} is {result}")

    result = math.factorial(5)
    print(f"factorial of 5 is {result}")

if __name__ == "__main__":
    main()