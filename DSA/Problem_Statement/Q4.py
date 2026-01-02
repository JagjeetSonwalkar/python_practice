# find the all possible unique sub_string where k = 3

def all_possible_string(s, k = 0):
    sub_string = []

    for left in range(len(s)):
        for right in range(left+1, len(s)-1):
            current_str = s[left:right]

            if len(current_str) == k and not current_str in sub_string:
                sub_string.append(current_str)

    print(sub_string)

def main():
    random_string = 'abcabcbb'

    all_possible_string(random_string, 3)

if __name__ == "__main__":
    main()