# Read File and Reverse Words in Each Line

import os

def reverse_word(file_name):
    if not os.path.exists(file_name):
        return False

    with open(file_name, 'r') as file:
        data = file.readlines()

    upgrade_data = []
    for line in data:
        words = line.strip().split()
        reverse_word = words[::-1]
        upgrade_line = " ".join(reverse_word)
        upgrade_data.append(upgrade_line + "\n")

    with open(file_name, 'w') as file:
        file.writelines(upgrade_data)

def main():
    file_name, ret = "", None

    file_name = input("Enter the file name: ")
    ret = reverse_word(file_name)

    if ret is not False:
        print("data reversed in file.")
    else:
        print("Unable to data reversed in file!")

if __name__ == "__main__":
    main()