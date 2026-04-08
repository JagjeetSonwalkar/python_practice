import os

class Files:
    def __init__(self, file_name):
        self.file_name = file_name
    
    #  Create and Write to a File
    def create_file(self):
        with open(self.file_name, 'w') as file:
            file.write("This file is created by python..")
            return True
        return False
    
    #  Read Entire File
    def read_file(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                data = file.read()
                return data
        return None
    
    # Read File Line by Line
    def read_file_by_line(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                data = file.readlines()
                return data
        return None

def main():
    ret = None
    file_obj = Files("jj.txt")

    # ret = file_obj.create_file()
    if ret:
        print("File is created or Already Exists")
    else:
        print("Unable to create the file!!")
    
    print("Reading the File...")
    ret = file_obj.read_file_by_line()
    for data in ret:
        print(data)



if __name__ == "__main__":
    main()