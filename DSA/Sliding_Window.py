# Maximum sum of subarray of size k using (Sliding window)

def max_sum_subarray(arr, k = 2,):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k] # arr[i - k] -> arr [0] -> x_value

        max_sum = max(max_sum, window_sum)

    return max_sum

def main():
    arr = [2, 1, 5, 1, 3, 2]
    k = 3

    ret = max_sum_subarray(arr, k)
    print(ret)


if __name__ == "__main__":
    main()