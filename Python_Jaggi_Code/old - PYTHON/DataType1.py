# Input: x = 25
# Output: Type of x is <class 'int'>

# Input: x = 12.5
# Output: Type of x is <class 'float'>

# Input: x = "Hello"
# Output: Type of x is <class 'str'>

# Input: x = True
# Output: Type of x is <class 'bool'>

# . Type conversion int → float
# Input: x = 5
# Output: 5.0

#  Type conversion float → int
# Input: x = 9.8
# Output: 9

# Q7. Type conversion string → int
# Input: x = "123"
# Output: 123

# Q8. Type conversion int → string
# Input: x = 99
# Output: "99"

# Q9. Check type of complex number
# Input: x = 3 + 4j
# Output: Type of x is <class 'complex'>

# Q10. Multiple variables assignment
# Input: a, b, c = 10, 20, 30
# Output: 10 20 30


if __name__ == "__main__":
    x = 25
    print(type(x))

    x = 12.5
    print(type(x))

    x = "Hello"
    print(type(x))

    x = True
    print(type(x))

    x = float(5)
    print(x)

    x = 9.8
    x = int(x)
    print(x)

    x = "123"
    x = int(x)
    print(x)

    x = 99
    x = str(x)
    print(x)

    x = 3 + 4j
    print(type(x))

    a, b, c = 10, 20, 30
    print(a,b,c)