import os
import sys
import time

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
    
    timestamp = time.ctime()

    log_file_name = "Jaggi_log%s.log"%(timestamp)
    log_file_name = log_file_name.replace(" ","_").replace(":","_")

    log_file = open(log_file_name, 'w')

    Border = "-"*54
    
    log_file.write(Border+"\n")
    log_file.write("This is a log file of Automation Script\n")
    log_file.write("This is a Directory Cleaner Script\n")

    log_file.write(Border+"\n")

    log_file.write("\n")
    data = "Total scanned file:" + str(total_file) + "\n"
    log_file.write(str(data))
    data = "Total Deleted file:" + str(deleted_file) + "\n"
    log_file.write(str(data))

    log_file.write("\n")

    log_file.write(Border+"\n")
    log_file.write("This is is created at \n"+timestamp+"\n")
    log_file.write(Border+"\n")

    log_file.close()


def main():
    Border = '-'*54
    print(Border)
    print("----------------Automation Started-------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the script as: ")
            print("ScriptName.py  NameOfDirctory")
            print("Please provide valid absolute path")

        else:
            directory_walkar(sys.argv[1])
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