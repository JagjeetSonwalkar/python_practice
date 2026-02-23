# Find First Non-Repeating Character
# Input 1 → "swiss" → Output 1 → 'w'
# Input 2 → "programming" → Output 2 → 'p'

# Remove All Vowels
# Input 1 → "education" → Output 1 → "dctn"
# Input 2 → "Industrial" → Output 2 → "ndstrl"

# Count Digits in String
# Input 1 → "Python123" → Output 1 → 3
# Input 2 → "AI2025" → Output 2 → 4

# Swap Case of String
# Input 1 → "Hello World" → Output 1 → "hELLO wORLD"
# Input 2 → "PythonAI" → Output 2 → "pYTHONai"

# Check if Two Strings are Anagrams
# Input 1 → "listen", "silent" → Output 1 → True
# Input 2 → "hello", "world" → Output 2 → False

def firstNonRepeatChar(getString):
    iCount = 0
    ch = ''
    for i in getString:
        ch = i
        for j in getString:
            if ch == j:
                iCount += 1
        if iCount == 1:
            return ch
        iCount = 0

def removeVowel(getString):
    newString = ""
    for i in getString:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            pass
        else:
            newString += i
    return newString

def countNum(getString):
    iCount = 0
    for i in getString:
        if i.isdigit():
            iCount += 1
    return iCount

def swapCase(getString):
    newString = ""
    for i in getString:
        if i.islower():
            newString += i.upper()
        elif i.isupper():
            newString += i.lower()
        else:
            newString += i
    return newString

def checkTwoStringAnagrams(getString1, getString2):
    list1 = list(getString1)
    list2 = list(getString2)

    list1.sort()
    list2.sort()

    return list1 == list2

def main():
    sentence, sentence2 = None, None
    Ret = None

    sentence = input("Enter the string: ")
    Ret = firstNonRepeatChar(sentence)
    print("First Non Repeating Char is: ",Ret)

    sentence = input("Enter the String: ").lower()
    sentence = removeVowel(sentence)
    print("new String after removing the vowel: ",sentence)

    sentence = input("Enter the String: ")
    Ret = countNum(sentence)
    print(f"Total digits in {sentence} is {Ret}")

    sentence = input("Enter the String: ")
    sentence = swapCase(sentence)
    print("after swap case: ",sentence)

    sentence = "listen".lower()
    sentence2 = "silent".lower()

    Ret = checkTwoStringAnagrams(sentence, sentence2)
    print(Ret)

if __name__ == "__main__":
    main()