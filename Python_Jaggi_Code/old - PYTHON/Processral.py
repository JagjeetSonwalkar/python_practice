def add(no1, no2):
    Ans = 0
    Ans = no1+no2;
    return Ans;

def main():
    print("Enter first number: ");
    no1 = int(input());

    print("Enter second number: ")
    no2 = int(input());

    iRet = add(no1, no2);

    print("Addition is: ",iRet);

if __name__ == "__main__":
    main()