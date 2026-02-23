# create new file
import os

def main():
    print("Enter the file name to create: ")
    fileName = input()

    iRet = os.path.exists(fileName)

    if(iRet == True):
        print("Unbale to create the file, file already exists !!")
        return
    else:
        myFile = open(fileName,'w')
        print("File created succesfully.")

        myFile.write("\nIndian is my country")

        myFile.close()
##############################################################

if __name__ == "__main__":
    main()