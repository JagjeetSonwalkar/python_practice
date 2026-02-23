# Count words in a sentence

def isEmpty(getString):
    if getString == None or getString.strip() == "":
        return True
    return False

def countWord(getString):
   
    if isEmpty(getString):
        print("String is Empty")
        return

    word = ''
    iCount = 0
    sentence = ''
    
    for i in getString:
        if(i != ' '):
            word += i
        elif(i == ' '):
            word += ' '
            sentence += word
            iCount += 1
            word = ''
    if(word != ''):
        sentence += word
        iCount += 1
    print(iCount)
    print(sentence)

if __name__ == "__main__":
    myString = "Apple is Not Blue "

    countWord(myString)