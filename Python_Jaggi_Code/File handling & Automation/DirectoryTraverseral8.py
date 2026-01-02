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

    total_file, deleted_file = 0, 0
    for folder, sub_folders, subfiles in os.walk(directory_name):
        for file in subfiles:
            total_file += 1
            if (os.path.getsize(os.path.join(folder, file))) == 0:
                os.remove((os.path.join(folder, file)))
                deleted_file += 1
    
    print("total file scanned:",total_file)
    print("total file deleted:",deleted_file)

def main():
    directory_name = input("Enter the directory that you want to travel: ")
    directory_walkar(directory_name)

if __name__ == "__main__":
    main()