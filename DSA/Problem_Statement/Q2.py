# find the all possible string where k = 3

def all_possible_string(s, k = 0):
    sub_string = []

    for left in range(len(s)):
        for right in range(left+1, len(s)):
            str = s[left:right]
            if len(str) == k:
                sub_string.append(str)

    print(sub_string)

def main():
    random_string = 'abcabcbb'

    all_possible_string(random_string, 2)

if __name__ == "__main__":
    main()