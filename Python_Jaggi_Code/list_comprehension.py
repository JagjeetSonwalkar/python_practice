# syntax : [ expression for value in iterable if condition ]

def main():
    numbers = [1, -2, 3, 40, -5, 60, 7, 80, 9, 10]
    fruits = ["apple", "banana", "orange", "strawberry", "peach", "coconut"]

    # create a list of square from 1 to 10
    squares = [num**2 for num in range(1,11)]
    print(squares)

    # make the all element of fruit in uppercase
    fruits = [fruit.upper() for fruit in fruits]
    print(fruits)

    # make the number all +ve
    numbers = [number for number in numbers if number > 0]
    print(numbers)

if __name__ == "__main__":
    main()