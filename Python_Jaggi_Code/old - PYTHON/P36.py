# 	Check if key exists
# 	Merge two dicts

def isKeyExists(getDict, getCheckValue):
    for iKey in getDict:
        if(getCheckValue == iKey):
            return True
    return False

if __name__ == "__main__":
    myDict = {1:2,2:4,3:6,4:8,5:10}

    checkKey = int(input("Enter the key for check it exists or not: "))

    Ret = isKeyExists(myDict, checkKey) # check key exists or not

    if(Ret == True):
        print("Key Exists")
    else:
        print("Key doesnt exists !")

    myDict2 = {11:1,12:3,13:5,14:7,15:11}
    myDict.update(myDict2) # merge two dicts

    print(myDict)

    