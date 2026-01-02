# Check if two numbers in an array add up to a given sum

def two_pointer(array, target):
    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]

        if current_sum == target:
            return array[left], array[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1


def main():
    list = [i for i in range(1, 50)]
    target = 6

    ret = two_pointer(list, target)
    print(f"two numbers in an array add up to a given sum: {target} is '{ret[0], ret[1]}'")

if __name__ == "__main__":
    main()