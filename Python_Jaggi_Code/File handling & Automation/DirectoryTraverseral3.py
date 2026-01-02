import os

def directoryWalker(getDirName):

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