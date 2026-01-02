# Merge sort

def merge_sort(arr, reverse = False):
    if len(arr) <= 1:
        return arr

    # divide
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # conquer
    left_sorted = merge_sort(left_arr, reverse)
    right_sorted = merge_sort(right_arr, reverse)

    # combine
    return merge(left_sorted, right_sorted, reverse)

def merge(left, right, reverse):
    result = []

    i = j = 0

    while i < len(left) and j < len(right):
        if reverse == False:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def main():
    list_of_num = [1, 2, 3, 42, 7, 19, 84, 3, 56, 91, 12, 68, 25, 14, 77, 5, 39, 88, 2, 73, 46, 30, 95, 11, 58, 4, 62, 27, 81, 9, 33, 70, 16, 53, 1, 99, 24, 63, 
    18, 85, 6, 49, 72, 13, 98, 34, 21, 57, 8, 90, 29, 75, 41]

    print(f"The orignal list is:\n{list_of_num}")

    list_of_num = merge_sort(list_of_num)
    print(f"The list after merge sort:\n{list_of_num}")

    list_of_num = merge_sort(list_of_num, True)
    print(f"The list aftermerge sort with reverse:\n{list_of_num}")

if __name__ == "__main__":
    main()