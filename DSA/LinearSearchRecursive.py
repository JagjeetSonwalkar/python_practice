# Linear Search - iteration

def linear_search(data, target_element, index = 0):
    if index == len(data):
        return -1                   # return -1 if not found
    
    if data[index] == target_element:
        return index

    return linear_search(data, target_element, index + 1)                      

def main():
    # list of 50 element
    list_of_num = [42, 7, 19, 84, 3, 56, 91, 12, 68, 25, 14, 77, 5, 39, 88, 2, 73, 46, 30, 95, 11, 58, 4, 62, 27, 81, 9, 33, 70, 16, 53, 1, 99, 24, 63, 
    18, 85, 6, 49, 72, 13, 98, 34, 21, 57, 8, 90, 29, 75, 41]

    find_element = int(input("Enter the element to check it is present or not: "))

    result = linear_search(list_of_num, find_element)

    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present!")

if __name__ == "__main__":
    main()