# Bubbel sort with combined condition for ASC & DESC

def bubble_sort(arr, reverse=False):
    size = len(arr)

    for i in range(size):
        for j in range(size-i-1):
            if reverse is False:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    # list of 50 element
    list_of_num = [1, 2, 3, 42, 7, 19, 84, 3, 56, 91, 12, 68, 25, 14, 77, 5, 39, 88, 2, 73, 46, 30, 95, 11, 58, 4, 62, 27, 81, 9, 33, 70, 16, 53, 1, 99, 24, 63, 
    18, 85, 6, 49, 72, 13, 98, 34, 21, 57, 8, 90, 29, 75, 41]

    print("list before bubbel sorted: ")
    print(list_of_num)

    list_of_num = bubble_sort(list_of_num, True)

    print("list in reverse bubble sorted: ")
    print(list_of_num)

    list_of_num = bubble_sort(list_of_num)

    print("list after bubbel sorted: ")
    print(list_of_num)

if __name__ == "__main__":
    main()