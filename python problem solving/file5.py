# delete the file
import os

def main():
    fileName = input("Enter the existing file Name to open: ")

    iRet = os.path.exists(fileName)

    if(iRet == True):
        os.remove(fileName)

        print("File gets Deleted.")
    else:
        print("File not exists!!")

if __name__ == "__main__":
    main()