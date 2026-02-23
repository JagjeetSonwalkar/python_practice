# Copy Content of One File to Another
# Merge Two Files

import os

def copy_file(src_file_name, des_file_name):
    if os.path.exists(des_file_name):
        return "Destenation file already exits!"
    if not os.path.exists(src_file_name):
        return "Source file not exists!"
    with open(src_file_name,'r') as src_file:
        data = src_file.read()
    with open(des_file_name,'w') as des_file:
        des_file.write(data)
    return True

def merge_file(first_file, second_file, new_file):
    if os.path.exists(new_file):
        return "result file exists"
    if not os.path.exists(first_file):
        return "first file does not exists"
    if not os.path.exists(second_file):
        return "second file does not exists"

    with open(first_file,'r') as file1, open(second_file, 'r') as file2:
        data = file1.read() + "\n" +file2.read()
   
    with open(new_file, 'w') as des_file:
        des_file.write(data)
    return True

def main():
    src_file_name, des_file_name, ret = None, None, None

    src_file_name = input("Enter file name that you want to copy: ")
    des_file_name = input("Enter the new file name to copy the content: ")
    
    ret = copy_file(src_file_name, des_file_name)

    if ret is True:
        print("file copied.")
    else:
        print(f"Unable to copy file because {ret}")

    print("merger two file")
    first_src_file_name = input("Enter first file name: ")
    second_src_file_name = input("Enter second file name: ")
    des_file_name = input("Enter file name that no exists to merger: ")

    ret = merge_file(first_src_file_name, second_src_file_name, des_file_name)

    if ret is True:
        print("File merged")
    else:
        print(f"Unable to merge the file because {ret}")

if __name__ == "__main__":
    main()