# . Count Substring Occurrences
# Input 1 → "ababab", "ab" → Output 1 → 3
# Input 2 → "python python", "python" → Output 2 → 2

# Remove Punctuation from String
# Input 1 → "Hello, World!" → Output 1 → "Hello World"
# Input 2 → "Python! is awesome." → Output 2 → "Python is awesome"

# Find All Palindromic Substrings
# Input 1 → "madam" → Output 1 → ["madam","ada"]
# Input 2 → "abba" → Output 2 → ["abba","bb"]

#  Reverse Words in a String
# Input 1 → "Hello World" → Output 1 → "World Hello"
# Input 2 → "Industrial Programming" → Output 2 → "Programming Industrial"

# Find Longest Word in a String
# Input 1 → "I love Python programming" → Output 1 → "programming"
# Input 2 → "Artificial Intelligence AI" → Output 2 → "Intelligence"

def countSubstringOccurrences(getString, getSubString):
    firstCharOfSubString = getSubString[0]
    lenghtofSubString = len(getSubString)
    word = ""
    iCount = 0

    for i in getString:
        if i == " ":
            pass
        else:
            word += i

        if len(word) == lenghtofSubString:
            if word == getSubString:
                iCount += 1
            word = ""
    
    return iCount

def removePunctuation(getString):
    newString = "" 
    for i in getString:
        if i.islower():
            newString += i
        elif i.isupper():
            newString += i
        elif i.isdigit():
            newString += i
        elif i == " ":
            newString += i
    
    return newString

def findSubStringPalindrom(getString):
    # check palindrom
    def isPalindrome(getString):
        orginalString = getString
        reverseString = getString[::-1]
        return orginalString == reverseString
    
    # remove first & last Char
    def removeFirstLastChar(getString):
        newString = ""
        for i in range(1,len(getString)-1,1):
            newString += getString[i]
        return newString

    orginalString = getString
    subStringPalindromList = []

    while(len(orginalString) >= 2):
        if isPalindrome(getString) == True:
            subStringPalindromList.append(orginalString)
        orginalString = removeFirstLastChar(orginalString)

    return subStringPalindromList

def reverseWord(getString):
    listOfWord = []
    word = ""
    newString = ""

    for i in getString:
        word += i
        if i == ' ':
            listOfWord.append(word)
            word = ""
    listOfWord.append(word)

    listOfWord.reverse()
    for words in listOfWord:
        newString += words
        newString += " "
    
    return newString

def findLogestWord(getString):
    word = ""
    maxWord = ""

    def getMax(getString):
        max = ""
        if len(maxWord) < len(getString):
            max = getString
        else:
            max = maxWord
        return max

    for i in getString:
        if i != ' ':
            word += i
       
        if i == " ":
            print(word)
            maxWord = getMax(word)
            word = ""
    maxWord = getMax(word)

    print(maxWord)
    return maxWord

def main():
    myString, subString = "", ""
    Ret = None

    print("<---- Count Substring Occurrences ---->")
    myString = input("Enter the String: ")
    subString = input("Enter the subString: ")
    Ret = countSubstringOccurrences(myString, subString)
    print(f"Count of substring '{subString}' occureences form the string'{myString}' is: {Ret}")

    print("<---- Remove Punctuation from String ---->")
    myString = input("Enter the String: ")
    print("String Before removing punctuation:",myString)
    myString = removePunctuation(myString)
    print("String After removing punctuation:",myString)

    myString = input("Enter the String: ")
    Ret = findSubStringPalindrom(myString)
    print("All Palindromic Substrings: ",Ret)

    myString = input("Enter the String: ")
    Ret = reverseWord(myString)
    print(f"'{myString}' after Reverse Words in a String: '{Ret}'")

    myString = input("Enter the String: ")
    Ret = findLogestWord(myString)
    print(f"Form the string '{myString}', the longest word is: '{Ret}'.")

if __name__ == "__main__":
    main()