def main():
    ## varaible
    num1, num2 = 20, 10
    ret = None
    data_list = [1,2,3,4]

    # Lambda to Add Two Numbers
    ret = lambda x, y : x+y
    print("Addition of two number:",ret(num1, num2)) 

    #  Lambda to Multiply Two Numbers
    ret = lambda x, y : x*y
    print("mul of two number:",ret(num1, num2))

    # Map with Lambda to Square Numbers in List
    ret = list(map(lambda x : x**2, data_list))
    print("square of list:",ret)

    # Map with Lambda to Double Numbers
    ret = list(map(lambda x:x*2, data_list))
    print("Double the list:",ret)

    # Filter Even Numbers Using Lambda
    ret = list(filter(lambda x : x%2 == 0, data_list))
    print("Even number:",ret)

    # Filter Odd Numbers Using Lambda
    ret = list(filter(lambda x : x % 2 != 0, data_list))
    print("Odd number:",ret)

    # Lambda to Find Maximum of Two Numbers
    ret = lambda x, y: x if x > y else y
    print(f"{num1} & {num2} max element is {ret(num1, num2)}")

    ## varibale updated
    data_list = ["rohit", "VIRAT", "hi", "duck"]

    # Map with Lambda to Convert Strings to Uppercase
    ret = list(map(lambda x : x.upper() if x.islower() else x.upper(), data_list))
    print(f"list of uppercase {ret}")

    # Filter Strings with Length > 3 Using Lambda
    ret = list(filter(lambda x: x if len(x) > 3 else None , data_list))
    print(f"Elements length greter than 3: {ret}")

    # Lambda to Check if Number is Positive
    # num1 = -1
    ret = lambda x : x >= 0
    print(f"Number is postive: '{ret(num1)}'")

if __name__ == "__main__":
    main()