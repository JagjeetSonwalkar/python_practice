# Print dictionary keys.
# Print dictionary values

if __name__ == "__main__":
    myDict = {1:"Rohit",2:"Virat",3:"Sky",4:"Hardik"}

    print(myDict.keys())
    print(myDict.values())

    for iKeys in myDict.keys():
        print(iKeys)

    for iValues in myDict.values():
        print(iValues)

    for value in myDict.items():
        print(value)

    for ikeys in myDict.keys():
        print("Keys:",ikeys,"values:",myDict[ikeys])
    