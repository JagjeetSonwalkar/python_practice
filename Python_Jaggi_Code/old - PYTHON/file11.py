# Read File in Reverse Order
# Replace Word in File
# Count Frequency of Word in File
# Find Lines Containing a Word

import os

def read_reverse(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = file.read()
        return data[::-1]
    return False

def replace_word_file(file_name, exist_word, replace_word):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = file.read()
            updated_data = data.replace(exist_word, replace_word)
        with open(file_name,'w') as file:
            file.write(updated_data)
        return True
    return False

def count_word(file_name, target_word):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = file.read().split()

        target_word = target_word.strip()   # FIX HERE

        iCount = 0
        for word in data:
            if word == target_word:
                iCount += 1

        return iCount
        
def line_word(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = file.readlines()
        
        single_word_list = []
        for sentence in data:
            if " " not in sentence and sentence != "\n":
                sentence = sentence.replace("\n","")
                single_word_list.append(sentence) 
        
        return single_word_list

def main():
    file_name, ret = None, None
    word = None

    # file_name = input("Enter the file name to read the data in reverse order: ")
    # ret = read_reverse(file_name)

    # if ret is not False:
    #     print('*'*100)
    #     print(ret) 
    #     print('*'*100)
    # else:
    #     print(f"unable to read file because {ret}")

    # file_name = input("Enter the file name to replace word: ")
    # exists_word = input("Enter the exists word: ")
    # replcae_word = input("Enter the replcae word: ")
    # ret = replace_word_file(file_name, exists_word, replcae_word)

    # if ret is not False:
    #     print('*'*100)
    #     print(ret) 
    #     print('*'*100)
    # else:
    #     print(f"unable to read file because {ret}")

    # file_name = input("Enter the file name to replace word: ")
    # word = input("Enter the word to count the frequency: ")

    # ret = count_word(file_name,word)
    # print(f"The count word '{word}' in file is '{ret}'")

    # file_name = input("Enter the file name to get single word in a line: ")
    # ret = line_word(file_name)
    # print(f"Lines Containing a Word are {ret} ")
   
if __name__ == "__main__":
    main()