# write in the existing file
import os

def main():
    print("Enter the file name to open: ")
    fileName = input()

    iRet = os.path.exists(fileName)

    if(iRet == True):
        print("File is open: ")
        MyFile = open(fileName,'w')

        writeData = input("Write the Data: ")

        MyFile.write(writeData)

        MyFile.close()

    else:
        print("There is no such file exists !!")

##############################################################

if __name__ == "__main__":
    main()