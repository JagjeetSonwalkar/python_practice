# Reverse a String
# Input 1 → "Hello" → Output 1 → "olleH"
# Input 2 → "Jagjeet" → Output 2 → "teejgaJ"

# Count Vowels in a String
# Input 1 → "OpenAI" → Output 1 → 3
# Input 2 → "Programming" → Output 2 → 3

# Convert String to Uppercase
# Input 1 → "hello world" → Output 1 → "HELLO WORLD"
# Input 2 → "java" → Output 2 → "JAVA"

# Convert String to Lowercase
# Input 1 → "HELLO" → Output 1 → "hello"
# Input 2 → "Python123" → Output 2 → "python123"

# Count Words in a String
# Input 1 → "I love Python" → Output 1 → 3
# Input 2 → "Industrial programming practice" → Output 2 → 3

def reverseX(getString):
    reverseString = ''
    for i in range(len(getString)-1,-1,-1):
        reverseString += getString[i]
    return reverseString

def countVowel(getString):
    iCount = 0
    for i in getString:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            iCount += 1
    return iCount

def toUpper(getString):
    upperString = ""
    asciiValue  = 0
    upperAsciiValue = 0

    for i in getString:
        asciiValue = ord(i)
        if 'a' <= i <= 'z':
            upperAsciiValue = asciiValue - 32
            upperString += chr(upperAsciiValue)
        else:
            upperString += i
    return upperString

def toLower(getString):
    lowerString = ""
    asciiValue = 0
    lowerAsciiValue = 0

    for i in getString:
        asciiValue = ord(i)
        if 'A' <= i <= 'Z':
            lowerAsciiValue = asciiValue + 32
            lowerString += chr(lowerAsciiValue)
        else:
            lowerString += i
    return lowerString

def countWord(getString):
    iCount = 0

    if getString[0] == ' ':
        iCount -= 1
    if getString[len(getString)-1] == ' ':
        iCount -= 1

    for i in getString:
        if i == ' ':
            iCount += 1
    iCount += 1
    return iCount



def main():
    Ret = None

    x = "Hello"
    x = reverseX(x)
    print(f"Reverse String: ",x)

    x = "Programming"
    Ret = countVowel(x)
    print(f"Count of Vowels in a String is: {Ret}")

    x = "time 12:30"
    x = toUpper(x)
    print(f"Upper String is: {x}")

    x = "IRON man 3"
    x = toLower(x)
    print(f"lower String is: {x}")

    x = "I Love Game 100-times "
    Ret = countWord(x)
    print(f"Total words in string: {x} is: {Ret}")

if __name__ == "__main__":
    main()