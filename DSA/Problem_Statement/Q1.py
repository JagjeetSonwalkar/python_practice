# find the all possible string

def all_possible_string(s):
    sub_string = []

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub_string.append(s[i:j])
    
    print(sub_string)


def main():
    random_string = 'abcabcbb'

    all_possible_string(random_string)

if __name__ == "__main__":
    main()