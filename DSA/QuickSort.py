# Quick sort

def quick_sort(arr, reverse=False):
    # Base case
    if len(arr) <= 1:
        return arr.copy()  # return a copy to avoid modifying original

    pivot = arr[-1]
    left = []
    right = []

    for x in arr[:-1]:
        if reverse:  # Descending
            if x >= pivot:
                left.append(x)
            else:
                right.append(x)
        else:        # Ascending
            if x <= pivot:
                left.append(x)
            else:
                right.append(x)

    # Recursively sort left and right, and combine with pivot
    return quick_sort(left, reverse) + [pivot] + quick_sort(right, reverse)

def main():
    list_of_num = [1, 2, 3, 42, 7, 19, 84, 3, 56, 91, 12, 68, 25, 14, 77, 5, 39, 88, 2, 73, 46, 30, 95, 11, 58, 4, 62, 27, 81, 9, 33, 70, 16, 53, 1, 99, 24, 63, 
    18, 85, 6, 49, 72, 13, 98, 34, 21, 57, 8, 90, 29, 75, 41]

    print(f"The orignal list is:\n{list_of_num}")

    list_of_num = quick_sort(list_of_num, False)
    print(f"The list after quick_sort:\n{list_of_num}")

    list_of_num = quick_sort(list_of_num, True)
    print(f"The list after quick_sort:\n{list_of_num}")

if __name__ == "__main__":
    main()