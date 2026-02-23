#	Replace spaces with - in input.

def main():
    Ret = None

    data = input("Enter the data: ")
    print("Orignal data: ",data)
    newRep = input("Replace space with: ")
    data = data.replace(" ",newRep)
    print("data after replace with space with '",newRep,"': ",data)

if __name__ == "__main__":
    main()