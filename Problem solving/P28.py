#   Print longest word from input.

def checkLongestWord(getString):
    wordList = []
    word = ''
    countWordList = []

    for i in getString:
        if(i != len(getString)):
            if(i != " "):
                word = str(word) + str(i)
            if(i == ' '):
                wordList.append(word)
                word = ''
    wordList.append(word)

    print(wordList)

    iCount = 0

    for i in range(len(wordList)):
        iCount = len(wordList[i]) 
        countWordList.append(iCount)
    print(countWordList)
           
    max = countWordList[0]
    index = 0
    for i in countWordList:
        if(max < i):
            max = i
    print(max)

    index = countWordList.index(max)
    print(index)

    return wordList[index]
    

def main():
    Ret = None

    Ret = checkLongestWord("Apple is big fruit! or not")
    print("The longest word from the string is: ",Ret)

if __name__ == "__main__":
    main()