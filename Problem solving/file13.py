'''
Count Lines Starting with a Specific Letter
Count Lines Ending with a Specific Letter
Read File and Count Digits
Read File and Count Alphabets
Read File and Count Special Characters
'''
import os
import string

def count_start_with(file_name, target_char):
    if not os.path.exists(file_name):
        return None
    
    with open(file_name, 'r') as file:
        data = file.readlines()

    if len(target_char) != 1:
        target_char = target_char[0]
    iCount = 0
    for line in data:
        line = line.replace("\n","")
        if line.startswith(target_char):
            iCount += 1
    return iCount

def count_end_with(file_name, target_char):
    if not os.path.exists(file_name):
        return None
    
    with open(file_name, 'r') as file:
        data = file.readlines()

    if len(target_char) != 1:
        target_char = target_char[0]
    iCount = 0
    for line in data:
        line = line.replace("\n","")
        if line.endswith(target_char):
            iCount += 1
    return iCount

def count_digit(file_name):
    if not os.path.exists(file_name):
        return None
    
    with open(file_name, 'r') as file:
        data = file.read()

    iCount = 0
    for i in range(len(data)):
        if data[i].isnumeric():
            iCount += 1
    return iCount

def count_alpha(file_name):
    if not os.path.exists(file_name):
        return None
    
    with open(file_name, 'r') as file:
        data = file.read()

    iCount = 0
    for i in range(len(data)):
        if data[i].isalpha():
            iCount += 1
    return iCount

def count_special(file_name):
    if not os.path.exists(file_name):
        return None
    
    with open(file_name, 'r') as file:
        data = file.read()

    # special_char = ('!','@','#','$','%','^','&','*','(',')','_','-','+','=','<','>',',''.','?','/',':',';','"',"'")
    special_char = set(string.punctuation)
    iCount = 0
    for i in range(len(data)):
        if data[i] in special_char:
            iCount += 1
    return iCount

def main():
    file_name, ret, char = None, None, ''

    file_name = input("Enter the file name: ")
    char = input("Enter the char: ")

    ret = count_start_with(file_name, char)
    print(f"The Count of Lines Starting with a Specific Letter '{char}' is '{ret}'")

    file_name = input("Enter the file name: ")
    char = input("Enter the char: ")

    ret = count_end_with(file_name, char)
    print(f"The Count of Lines ends with a Specific Letter '{char}' is '{ret}'")

    file_name = input("Enter the file name: ")
    ret = count_digit(file_name)
    print(f"Count of Digits is {ret}")

    file_name = input("Enter the file name: ")
    ret = count_alpha(file_name)
    print(f"Count of digits is {ret}")

    file_name = input("Enter the file name: ")
    ret = count_special(file_name)
    print(f"Count of special char is {ret}")

if __name__ == "__main__":
    main()