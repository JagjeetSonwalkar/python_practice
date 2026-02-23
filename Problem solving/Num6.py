#  Find GCD of Two Numbers

def findGCD(getNum1, getNum2):
    i = 1
    while i <= getNum1 and i <= getNum2:
        if (getNum1 % i == 0 and getNum2 % i == 0):
            gcd = i
        i += 1
            
    print(gcd)

def main():
    Ret = 0
    num1, num2 = 0, 0

    num1 = int(input("Enter the number first number to find GCD: "))
    num2 = int(input("Enter the number second number to find GCD: "))
    findGCD(num1, num2)

if __name__ == "__main__":
    main()