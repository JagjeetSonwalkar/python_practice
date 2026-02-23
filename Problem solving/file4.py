# Read data from the existing file
import os

def main():
    fileName = input("Enter the existing file Name to open: ")

    iRet = os.path.exists(fileName)

    if(iRet == True):
        print("File exists: ")
        MyFile = open(fileName,'r')

        readData = MyFile.read()

        print("Data inside file is: ",readData)

if __name__ == "__main__":
    main()