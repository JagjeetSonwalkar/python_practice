# Remove Leading and Trailing Spaces
# Input 1 → " hello " → Output 1 → "hello"
# Input 2 → " Python AI " → Output 2 → "Python AI"

#  Count Number of Sentences
# Input 1 → "Hello world. How are you?" → Output 1 → 2
# Input 2 → "This is AI. Industrial programming is fun." → Output 2 → 2

#  Extract Numbers from String
# Input 1 → "Python123AI456" → Output 1 → [123, 456]
# Input 2 → "AI2025Data45" → Output 2 → [2025, 45]

# Replace Multiple Spaces with Single Space
# Input 1 → " Hello World" → Output 1 → " Hello World"
# Input 2 → "  Python  AI Rocks  " → Output 2 → "Python AI Rocks"


def countSentence(getString):
    iCount = 0

    for i in getString:
        if i == ".":
            iCount += 1
        elif i == "?":
            iCount += 1
        elif i == "!":
            iCount += 1
    
    return iCount

def extractNum(getString):
    num = ""
    numList = []

    for i in getString:
        if i.isdigit():
            num += i
        else: 
            if num != '':
                numList.append(num)
            num = ""
    if num.isdigit():
        numList.append(num)
    
    return numList

def multispaceToSinglespace(getString):
    newString = getString
    newString = " ".join(newString.split())
    return newString

def main():
    myString = ""
    Ret = None

    myString = input("Enter the String: ")
    Ret = myString.strip() # Remove Leading and Trailing Spaces
    print(f"old String '{myString}' & length is:{len(myString)},new String '{Ret}' & length is:{len(Ret)}")

    myString = input("Enter the String: ")
    Ret = countSentence(myString)
    print(f"Total count of sentence in String '{myString}' is '{Ret}'")

    myString = input("Enter the String: ")
    Ret = extractNum(myString)
    print(f"String '{myString}',After Extract Numbers from String:'{Ret}'")

    Ret = multispaceToSinglespace("  Hello  World  ")
    print(Ret)
    
if __name__ == "__main__":
    main()