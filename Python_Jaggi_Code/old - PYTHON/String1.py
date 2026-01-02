
# extract the string and return first and last name's
def removeSpecialChar(getMyStr):
    newString = ""
    firstName = ""
    lastName = ""
    for i in getMyStr:
        if i.isalpha():
            newString += i

    firstName += newString[0]
    for i in range(1,len(newString),1):
        if(newString[i].isupper() and i != 0):
            firstName = newString[:i]
            lastName = newString[i:]
            break

    return firstName, lastName

# max char occurance & return the max char
def maxChar(getStr):
    myDict = dict()

    for i in getStr:
        if myDict.keys() != i:
            myDict.update({i:0})

    for i in getStr:
        if i in myDict:
            myDict[i] += 1

    max_Key, max_Value = list(myDict.keys())[0], list(myDict.values())[0]

    i = 0
    for i, j in myDict.items():
        if max_Value < j:
            max_Value = j
            max_Key = i

    return max_Key, max_Value

def main():
    Ret1, Ret2 = 0, 0

    myStr = "^$#&@Hardik^*&$(57)Pandya"
    firstName, lastName = "", ""

    firstName, lastName = removeSpecialChar(myStr)
    print(f"First Name: {firstName}, Last Name: {lastName}")
    
    Ret1, Ret2 = maxChar("RohitSharma")
    print(f"The max occurens of character is: '{Ret1}' with {Ret2} times")

if __name__ == "__main__":
    main()