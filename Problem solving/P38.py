# Write a Python program to generate n random number
import random

def n_number(n = 1, start = 1, end = 100):
    random_num = []
    for i in range(n):
        random_num.append(random.randint(start, end))
    return random_num

#Write a Python program to find N largest elements from a list.
def n_max(nums, n):
    sorted_num = sorted(nums, reverse=True)
    n_max_num = sorted_num[len([sorted_num[n]])]
    
    return n_max_num

# Write a Python program to Remove empty List from List.
def remove_empty(lit):
    result_list = [
        i for i in lit if i
    ]
    return result_list

# remove special char
def remove_special_char(chars):
    special_char = '!@#$%^&*()_+-={[}]":";?><,./~`'
    new_chars = ""

    for x in chars:
        if x not in special_char and x != "'":
            new_chars += x
    return new_chars


    new_chars = [
        x for x in chars if x not in special_char
    ]
    return new_chars.t

def main():
    result = n_number(n = 10)
    print(result)

    nums = [n for n in range(1, 101)]
    result = n_max(nums, 2)
    print("n max number is:",result)

    list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
    list_of_lists = remove_empty(list_of_lists)
    print(list_of_lists)

    name = "da't:'es"
    name = remove_special_char(name)
    print(name)

if __name__ == "__main__":
    main()