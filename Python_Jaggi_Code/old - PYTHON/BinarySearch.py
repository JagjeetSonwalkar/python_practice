# binary Search - with sorted data

def binary_search(data, target_element):
    if len(data) == 0:
        return -1

    index, size = 0, len(data)-1

    while(index <= size):
        mid = (index + size) // 2

        if data[mid] == target_element:
            return mid
        
        elif target_element < data[mid]:
            size = mid - 1
        else:
            index = mid + 1

    return -1


def main():
    num_list = [3, 5, 7, 9, 12, 14, 17, 19, 21, 24, 27, 29, 31, 33, 36, 38, 41, 43, 45, 47, 50, 52, 55, 57, 60, 62, 64, 67, 69, 72, 74, 77, 79, 82, 84, 87, 89, 92, 
    94, 97, 100, 103, 105, 108, 110, 112, 115, 118, 120, 123]

    search_element = int(input("Enter the element to search: "))

    ret = binary_search(num_list, search_element)

    if ret != -1:
        print(f"Element is present at index {ret}")
    else:
        print("Element not found!")

if __name__ == "__main__":
    main()