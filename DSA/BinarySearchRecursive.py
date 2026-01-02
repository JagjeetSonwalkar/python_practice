# binary Search - with sorted data

def binary_search(data, target_element, size, index = 0):
    if len(data) == 0:
        return -1

    mid = (index + size) // 2

    if index <= size:
        
        # check mid element
        if data[mid] == target_element:
            return mid
        
        # search left half
        elif target_element < data[mid]:
            return binary_search(data, target_element, mid - 1, index)
            
        # search right half
        else:
            return binary_search(data, target_element, size, mid + 1)   
    return -1

def main():
    num_list = [3, 5, 7, 9, 12, 14, 17, 19, 21, 24, 27, 29, 31, 33, 36, 38, 41, 43, 45, 47, 50, 52, 55, 57, 60, 62, 64, 67, 69, 72, 74, 77, 79, 82, 84, 87, 89, 92, 
    94, 97, 100, 103, 105, 108, 110, 112, 115, 118, 120, 123]

    # num_list = [0, 10]

    search_element = int(input("Enter the element to search: "))

    ret = binary_search(num_list, search_element, len(num_list))

    if ret != -1:
        print(f"Element is present at index {ret}")
    else:
        print("Element not found!")

if __name__ == "__main__":
    main()