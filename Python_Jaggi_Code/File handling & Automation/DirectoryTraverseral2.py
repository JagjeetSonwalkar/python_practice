import os

def directoryWalker():

    for mainFolder, subFolder, fileNames in os.walk("Jaggi"):
        print("Main folder name is: "+mainFolder)

        for subF in subFolder:
            print("Sub folder name is: "+subF)
        
        for fName in fileNames:
            print("File name is: "+fName)

def main():
    directoryWalker()

if __name__ == "__main__":
    main()