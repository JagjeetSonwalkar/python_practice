# Append Text to Existing File

import os

def write_data(file_name, data, append=True):
    if os.path.exists(file_name):
        mode = 'a' if append else 'w'
        with open(file_name, mode) as file:
            file.write(data)
        return True
    return False

def main():
    name_of_file, ret = None, None

    name_of_file = input("Enter the file name to write data: ")
    data_of_file = input("Write the data insert into file: ")
    ret = write_data(name_of_file, data_of_file)

    if ret is True:
        print("Data wrote succesfully")
    else:
        print("Unable to write data!")

if __name__ == "__main__":
    main()