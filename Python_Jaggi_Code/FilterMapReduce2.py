from functools import reduce

def main():
    ## varaible
    ret = None
    data_list = [1,2,3,4,5]

    # Reduce to Compute Sum of List
    ret = reduce(lambda x, y : x+y, data_list)
    print(f"Sum of list {ret}")
   
   # Reduce to Compute Product of List
    ret = reduce(lambda x, y: x*y, data_list)
    print(f"Product of list {ret}")

    # Map with Lambda to Add 5 to Each Element
    ret = list(map(lambda x : x + 5, data_list))
    print(f"After adding 5 to each element: {ret}")

    data_list = ["python", "pdf", "pi", "time", "ipl"]

    # Filter Strings Starting with 'p'
    ret = list(filter(lambda x : x if x[0] == 'p' else None,data_list))
    print(f"element start with 'p' in list are: {ret}")

    # Map with Lambda to Reverse Strings
    ret = list(map(lambda x : x[::-1], data_list))
    print(f"revser each element of list: {ret}")

    data_list = [1,20,3,40,5]

    # Filter Numbers Greater than 10
    ret = list(filter(lambda x :x if x > 10 else None, data_list))
    print(f"Number of list that are greater than '10': {ret}")

    # Reduce to Find Maximum Number
    ret = reduce(lambda x, y : x if x>y else y, data_list)
    print(f"Max element of list is: {ret}")

if __name__ == "__main__":
    main()