import os

def main():

    for mainFolder, subFolder, fileNames in os.walk("Jaggi"):
        print("Folder name is: "+mainFolder)

        for subF in subFolder:
            print("Sub folder: "+subF)

        for fNames in fileNames:
            print("file Names: "+fNames)

if __name__ == "__main__":
    main()