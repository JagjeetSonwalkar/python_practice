import os

def directoryWalker(getDirName):

    flag = os.path.isabs(getDirName)

    if flag is False:
        getDirName = os.path.abspath(getDirName)
    
    flag = os.path.exists(getDirName)

    if flag is False:
        print("The path is invalid")
        exit()

    flag = os.path.isdir(getDirName)

    if flag == False:
        print("path is valid but the target is not a directory.")
        exit()

    print("absoult path:",getDirName)

    for mainFolder, subFolder, fileNames in os.walk(getDirName):
        print("Main folder name is: "+mainFolder)

        for subF in subFolder:
            print("Sub folder name is: "+subF)
        
        for fName in fileNames:
            print("File name is: "+fName)

def main():
    dirName = input("Enter the directory name to travel: ")

    directoryWalker(dirName)

if __name__ == "__main__":
    main()