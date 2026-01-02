#	Remove spaces from input string

def main():
    string = None

    string = input("Enter your full name: ")

    string = string.replace(' ','')

    print("String with out space: ",string)


if __name__ == "__main__":
    main()