# Write List of Strings to File
# Input 1 → List: ['a','b','c'] → File content → "a\nb\nc"
# Input 2 → List: ['x','y'] → File content → "x\ny"

# Read File and Store Lines in List Without Newline
# Input 1 → File content: "Hello\nWorld" → Output 1 → ['Hello','World']
# Input 2 → File content: "A\nB\nC" → Output 2 → ['A','B','C']

#  Find Longest Line in File
# Input 1 → File content: "Hi\nHello\nWorld!" → Output 1 → "World!"
# Input 2 → File content: "A\nPython Rocks\nC" → Output 2 → "Python Rocks"

# 27. Find Shortest Line in File
# Input 1 → File content: "Hi\nHello\nWorld" → Output 1 → "Hi"
# Input 2 → File content: "Python\nC\nJava" → Output 2 → "C

import os

def list_to_file(file_name, list_of_word):
    if not os.path.exists(file_name):
        return False

    updated_list = []
    for sentence in list_of_word:
        sentence += "\n"
        updated_list.append(sentence)

    with open(file_name, 'a') as file:
        file.writelines(updated_list)
    return True

def file_to_list(file_name):
    if not os.path.exists(file_name):
        return False
    
    with open(file_name, 'r') as file:
        data = file.read().splitlines()
    
    return data

def get_longest_line(file_name):
    if not os.path.exists(file_name):
        return "file dont exists"

    with open(file_name, 'r') as file:
        data = file.readlines()

    max_length = data[0].replace("\n","")
    for sentence in data:
        sentence = sentence.replace("\n","")
        if len(max_length) < len(sentence) and sentence != "":
            max_length = sentence
        
    return max_length

def get_short_line(file_name):
    if not os.path.exists(file_name):
        return "file dont exists"

    with open(file_name, 'r') as file:
        data = file.readlines()

    short_line = data[0].replace("\n","")
    for sentence in data:
        sentence = sentence.replace("\n","")
        if len(short_line) > len(sentence) and sentence != "":
            short_line = sentence
    return short_line

def main():
    file_name, ret = None, None

    word_list = ["hello", "ram", "how are you", "i am file what about you", "same"]

    file_name = input("Enter the file name to write data of list in it: ")
    ret = list_to_file(file_name, word_list)

    if ret is True:
        print("Data written succesfully.")
    else:
        print("Unable to write data.")

    file_name = input("Enter the file name to read data in list format: ")
    ret = file_to_list(file_name)
    if ret is not False:
        print(f"Data in list format without new-line:\n{ret}")
    else:
        print("Unable to read the data")

    file_name = input("Enter the file name to get max line: ")
    ret = get_longest_line(file_name)
    if ret is not False:
        print(f"The max line is '{ret}'")
    else:
        print("Unable to get max line!")

    file_name = input("Enter the file name to get short line: ")
    ret = get_short_line(file_name)
    if ret is not False:
        print(f"The short line is '{ret}'")
    else:
        print("Unable to get short line!")

if __name__ == "__main__":
    main()