import os

def directory_watcher(dir_name):
    flag = os.path.isabs(dir_name)

    if flag is False:
        dir_name = os.path.abspath(dir_name)
    
    flag = os.path.exists(dir_name)

    if flag is False:
        print("The path is invalid")
        exit()

    if flag == False:
        print("path is valid but the target is not a directory")
        exit()

    print("Absolute path is:",dir_name)

    for folder_name, sub_folder_names, file_names in os.walk("testing_folder"):
        print(f"Folder name : {folder_name}")

        for folder_names in sub_folder_names:
            print(f"Sub folder : {folder_names}")

        for file_name in file_names:
            print(f"file name : {file_name}")

        print()

dir_name = input()
directory_watcher(dir_name)