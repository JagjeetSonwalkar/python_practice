import os
import sys
import time

def directory_walkar(directory_name, target_extension):
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
            if file.endswith(target_extension):
                os.remove(os.path.join(folder, file))
        
def main():
    Border = '-'*54
    print(Border)
    print("----------------Automation Started-------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning with given extenstion")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the script as: ")
            print("ScriptName.py  NameOfDirctory Expected_Extention")
            print("Please provide valid absolute path")

    elif(len(sys.argv) == 3):
            directory_walkar(sys.argv[1], sys.argv[2])
    else:
        print("Invalid number of Command Line argument !")
        print("Use the given flags: ")
        print("--h: used to display the help")
        print("--u: used to display the usage")

    print(Border)
    print("-------Thank you for using Script-----------")
    print(Border)

if __name__ == "__main__":
    main()