#	Count words in a sentence
# 	Print input string in uppercase.
#	Print input string in lowercase
# 	Count vowels in a string.

def countWords(getString):
    iCount = 0

    for i in getString:
        if i.isalpha():
            iCount += 1
    return iCount

def countVowels(getString):
    iCount = 0

    for value in getString:
        if(value == 'a'or value == 'e' or value == 'i' or value == 'o' or value == 'u' or value == 'A' or value == 'E' or value == 'I' or value == 'O' or value == 'U'):
            iCount = iCount + 1
    return iCount

def main():
    Ret = 0

    sSentence = "I Love Mountain" #13

    Ret = countWords(sSentence)

    print("Sentence: ",sSentence)
    print("Total words in the sentence are: ",Ret)

    name = input("Enter the name: ").lower()
    print("My name is: ",name)

    name = input("Enter full name: ").upper()
    print("My full name is: ",name)

    Ret = countVowels("AEIou")
    print("Total vowel are: ",Ret)

    Ret = countVowels("aeiou")
    print("Total vowel are: ",Ret)

    Ret = countVowels("apple")
    print("Total vowel are: ",Ret)

if __name__ == "__main__":
    main()
