# Check if String is Palindrome
# Input 1 → "madam" → Output 1 → True
# Input 2 → "hello" → Output 2 → False

# Remove Spaces from a String
# Input 1 → "Open AI Chat" → Output 1 → "OpenAIChat"
# Input 2 → "Industrial Programming" → Output 2 → "IndustrialProgramming"

# Count Occurrences of a Character
# Input 1 → "banana", char 'a' → Output 1 → 3
# Input 2 → "programming", char 'g' → Output 2 → 2

def isPalindrome(getString):
    orignalString = getString
    reversedString = ""

    for i in range(len(getString)-1,-1,-1):
        reversedString += getString[i]
    
    return orignalString == reversedString

def removeSpace(getString):
    newString = ""
    for i in getString:
        if i != " ":
            newString += i
    return newString

def occurrencesOfChar(getString, getChar):
    iCount = 0
    for i in getString:
        if getChar == i:
            iCount += 1
    return iCount

def main():
    Ret = None
    inputString, replaceString = None, None

    x = "madam"
    x = "hello"

    Ret = isPalindrome(x)
    if Ret == True:
        print("it is an palindrome")
    else:
        print("it is not an palindrome")
    
    x = " I am Jack ?"
    x = removeSpace(x)
    print(x)


    x = "banana"
    myChar = 'a'
    Ret = occurrencesOfChar(x,myChar)
    print(f"occurences of {myChar} is: {Ret}")


if __name__ == "__main__":
    main()