# 	Create a dictionary.
# 	Access value by key.
# 	Add new key-value pair.
# 	Delete key.
# 	Update value.
# 	Print keys.
# 	Print values.
# 	Print items.
# 	Length of dictionary

if __name__ == "__main__":
    myDict = dict()

    myDict[1] = "Rohit"

    myDict[2] = "Jack"

    myDict[0] = "Will"

    print(myDict)

    myDict.update({0:"Duck"})

    print(myDict)

    print("Keys:",myDict.keys())

    print("Values:",myDict.values())

    print("items:",myDict.items())

    print("Lenght of dict is:",len(myDict))

