# Rename a File
# Get File Size
# Check if File is Readable

import os

def rename_file(existsing_file_name, new_file_name):
    if os.path.exists(existsing_file_name):
        os.rename(existsing_file_name, new_file_name)
        return True
    return False

def get_size(file_name):
    if os.path.exists(file_name):
        file_size, mb_size = 0, 0

        file_size = os.path.getsize(file_name)
        kb_size = file_size / 1024
        mb_size = file_size / (1024*1024)
        return kb_size
    return None

def is_readable(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return True
    return False

def main():
    file_name, ret, new_file_name = None, None, None

    file_name = input("Enter the existsing file name: ")
    new_file_name = input("Enter new name for rename the file name: ")

    ret = rename_file(file_name, new_file_name)

    if ret == True:
        print("file renamed.")
    else:
        print("unable to read the name!")

    file_name = input("Enter the file name to get size: ")
    ret = get_size(file_name)

    if ret is not None:
        print(f"size of file is {ret:.2f} KB")
    else:
        print("Unable to get size of file!")

    file_name = input("Enter the file name to check it is readable or not: ")
    ret = is_readable(file_name)
    if ret is True:
        print("File is readable")
    else:
        print("Unable to read the file")

if __name__ == "__main__":
    main()