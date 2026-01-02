# Insertion sort

def insertion_sort(arr, reverse = False):
    size = len(arr)

    for i in range(size):
        key = arr[i] 
        j = i - 1

        if reverse is False:
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
        else:
            while j >= 0 and arr[j] < key:
                arr[j+1] = arr[j]
                j -= 1

        arr[j+1] = key
    return arr

def main():
    list_of_num = [1, 2, 3, 42, 7, 19, 84, 3, 56, 91, 12, 68, 25, 14, 77, 5, 39, 88, 2, 73, 46, 30, 95, 11, 58, 4, 62, 27, 81, 9, 33, 70, 16, 53, 1, 99, 24, 63, 
    18, 85, 6, 49, 72, 13, 98, 34, 21, 57, 8, 90, 29, 75, 41]

    print(f"The orignal list is:\n{list_of_num}")

    list_of_num = insertion_sort(list_of_num)
    print(f"The list after insertion sort:\n{list_of_num}")

    list_of_num = insertion_sort(list_of_num, True)
    print(f"The list after insertion sort with reverse:\n{list_of_num}")

if __name__ == "__main__":
    main()