import os

def directory_walkar(directory_name):
    flag = os.path.isabs(directory_name)

    if flag == False:
        directory_name = os.path.abspath(directory_name)
    
    flag = os.path.exists(directory_name)

    if flag == False:
        print("path is invalid !")
        exit()
    
    flag = os.path.isdir(directory_name)

    if flag == False:
        print("path is valid but target directory not exists")
    
    print("Absoult path:",directory_name)

    for folder, sub_folders, subfiles in os.walk(directory_name):
        for file in subfiles:
            print("file name:",file)
            print("file size:",os.path.getsize(file),"bytes")   # ERROR

def main():
    directory_name = input("Enter the directory that you want to travel: ")
    directory_walkar(directory_name)

if __name__ == "__main__":
    main()