# Create a list of squares of numbers from 1 to 10.

def squareList():
    square = []

    for i in range(1,10+1,1):
        square.append(i**2)

    return square

def main():
    Ret = 0

    Ret = squareList()

    print("Square list from 1 to 10 is: ",Ret)


if __name__ == "__main__":
    main()