# Heap sort

def heap_sort(arr, reverse=False):
    n = len(arr)

    # Build a heap (Max or Min depending on reverse)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, reverse)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        heapify(arr, i, 0, reverse)

    return arr
    
def heapify(arr, n, i, reverse):
    largest_or_smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if not reverse:  
        if left < n and arr[left] > arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] > arr[largest_or_smallest]:
            largest_or_smallest = right
    else: 
        if left < n and arr[left] < arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] < arr[largest_or_smallest]:
            largest_or_smallest = right

    # If root is not largest/smallest
    if largest_or_smallest != i:
        arr[i], arr[largest_or_smallest] = arr[largest_or_smallest], arr[i]
        heapify(arr, n, largest_or_smallest, reverse)

def main():
    list_of_num = [1, 2, 3, 42, 7, 19, 84, 3, 56, 91, 12, 68, 25, 14, 77, 5, 39, 88, 2, 73, 46, 30, 95, 11, 58, 4, 62, 27, 81, 9, 33, 70, 16, 53, 1, 99, 24, 63, 
    18, 85, 6, 49, 72, 13, 98, 34, 21, 57, 8, 90, 29, 75, 41]

    print(f"The orignal list is:\n{list_of_num}")

    list_of_num = heap_sort(list_of_num, False)
    print(f"The list after heap sort:\n{list_of_num}")

    list_of_num = heap_sort(list_of_num, True)
    print(f"The list after heap sort:\n{list_of_num}")

if __name__ == "__main__":
    main()