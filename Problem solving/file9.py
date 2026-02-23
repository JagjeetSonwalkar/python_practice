#  Read N Characters from File
#  Count Number of Lines in File
# Count Number of Words in File
# Count Number of Characters in File

import os

def read_file(file_name, size):
    if not os.path.exists(file_name):
        return False
    with open(file_name, 'r') as file:
        data = file.read()
    return data[:size]

def count_lines(file_name):
    if not os.path.exists(file_name):
        return False
    with open(file_name, 'r') as file:
        data = file.readlines()
    return len(data)

def count_word(file_name):
    if not os.path.exists(file_name):
        return False
    with open(file_name, 'r') as file:
        data = file.read().split()
    return len(data)

def count_char(file_name):
    if not os.path.exists(file_name):
        return False
    with open(file_name, 'r') as file:
        data = file.read()
        filter_data = data.replace(" ","").replace("\n","")
    return len(filter_data)


def main():
    file_name, ret, read_size = None, None, None

    file_name = input("Enter the name of file to read data:")
    read_size = int(input("Enter the size to read the N charcters: "))
    ret = read_file(file_name, read_size)

    if ret == False:
        print("Unable to read data into file !")
    else:
        print("Data read form the file is: ")
        print("-"*50)
        print(ret)
        print("-"*50)

    file_name = input("Enter the name of file to read data:")
    ret = count_lines(file_name)
    if ret is not False:
        print("No. of lines in file is:",ret)
    else:
        print("Unable to count file!")

    file_name = input("Enter the name of file to count words:")
    ret = count_word(file_name)
    if ret is not False:
        print("Total words in file are:",ret)
    else:
        print("Unable to count word!")

    file_name = input("Enter the name of file to count character:")
    ret = count_char(file_name)
    if ret is not False:
        print("Total character in file are:",ret)
    else:
        print("Unable to count character!")

if __name__ == "__main__":
    main()