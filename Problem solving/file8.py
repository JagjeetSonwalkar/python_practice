# Write Multiple Lines to File

import os

def write_file(file_name):
    if not os.path.exists(file_name):
        return False

    data = []
    enter_count = 0
    line = None

    print("Write the data: ")
    print("-"*100)
    while True:
        line = input().strip()
        if line == "":
            enter_count += 1
            if enter_count == 2:
                break
        else:
            enter_count = 0
        data.append(line)
    print("-"*100)

    with open(file_name, 'w') as file:
        file.write("\n".join(data))

def main():
    file_name, ret = None, None

    file_name = input("Enter the name of file to write data:")
    ret = write_file(file_name)

    if ret == False:
        print("Unable to write data into file !")
    else:
        print("Data writen into file")



    
if __name__ == "__main__":
    main()