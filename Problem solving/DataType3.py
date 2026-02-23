# Q23. Complex multiplication
# Input: (1+2j) * (2+3j)
# Output: -4+7j

# Q24. Get ASCII value of character
# Input: 'A'
# Output: 65

# Q25. Convert ASCII to char
# Input: 66
# Output: 'B'

# Q26. Convert string to list of chars
# Input: "CAT"
# Output: ['C','A','T']

# Q27. Check numeric string
# Input: "12345"
# Output: True

# Q28. Check alphabetic string
# Input: "Python"
# Output: True

# Q29. Check alphanumeric string
# Input: "P123"
# Output: True

# Q30. Convert boolean to int
# Input: True
# Output: 1

if __name__ == "__main__":
    ans = (1+2j) * (2+3j)
    print(ans)

    a = 'A'
    print(ord(a))

    a = 66
    print(chr(a))

    a = "CAT"
    print(list(a))

    a = "12345"
    if(a.isnumeric):
        print(True)
    else:
        print(False)

    a = "Python"
    if(a.isalpha):
        print(True)
    else:
        print(False)

    a = "P123"
    if(a.isalnum):
        print(True)
    else:
        print(False)

    a = True
    convertToInt = int(a)
    print(convertToInt)
