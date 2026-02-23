# Remove Duplicate Characters
# Input 1 → "programming" → Output 1 → "progamin"
# Input 2 → "banana" → Output 2 → "ban"

#  Count Uppercase and Lowercase Letters
# Input 1 → "HelloWorld" → Output 1 → Uppercase: 2, Lowercase: 8
# Input 2 → "PythonAI" → Output 2 → Uppercase: 3, Lowercase: 5

# Check if String Contains Only Digits
# Input 1 → "12345" → Output 1 → True
# Input 2 → "Python123" → Output 2 → False

# Merge Two Strings Alternately
# Input 1 → "abc", "123" → Output 1 → "a1b2c3"
# Input 2 → "Hello", "World" → Output 2 → "HWeolrllod"


def removeDuplicateChar(getString):
    newChar = ''
    newString = ""
    for char in getString:
        newChar = char
        if char in newString:
            pass
        else:
            newString += char
    
    return newString

def countUpperLowerCases(getString):
    countUpperCase, countLowerCase = 0, 0

    for i in getString:
        if i.isupper():
            countUpperCase += 1
        elif i.islower():
            countLowerCase += 1
    
    return countUpperCase, countLowerCase

def strContainOnlyDigit(getString):
    for i in getString:
        if i.isdigit():
            pass
        else:
            return False
    return True

def mergeStringAlt(getString1, getString2):
    newString = ""
    
    if len(getString1) != len(getString2):
        print("! lenght of both string should be same.")
        return False

    for i in range(len(getString1)):
        newString += getString1[i]
        newString += getString2[i]
    
    return newString


def main():
    word, Ret = None, None
    Ret2 = None
    word2 = None

    word = input("Enter the String: ")
    Ret = removeDuplicateChar(word)
    print("After removing duplicate characters: ",Ret)

    word = input("Enter the String: ")
    Ret, Ret2 = countUpperLowerCases(word)
    print(f"from the string: {word} the upperCase char count is: {Ret} & the lower case count is: {Ret2}")

    word = input("Enter the String: ")
    Ret = strContainOnlyDigit(word)
    if Ret == True:
        print("The string contain only digits")
    else:
        print("The string not contain all digits")

    word = input("Enter the 1st String: ")
    word2 = input("Enter the 2nd String: ")
    Ret = mergeStringAlt(word, word2)
    print("Merger string is: ",Ret)


if __name__ == "__main__":
    main()