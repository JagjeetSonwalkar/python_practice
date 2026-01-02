# Add int and float
# Input: a = 10, b = 2.5
# Output: 12.5

# Concatenate two strings
# Input: "Hello" "World"
# Output: "HelloWorld"

# Q13. Multiply string with int
# Input: "Hi" * 3
# Output: "HiHiHi"

# Q14. Boolean operations (AND)
# Input: True and False
# Output: False

# Q15. Boolean operations (OR)
# Input: False or True
# Output: True

# Q16. Boolean operations (NOT)
# Input: not True
# Output: False

# Q17. Automatic type promotion
# Input: 5 + 3.5
# Output: 8.5

# Q18. String to float conversion
# Input: "45.9"
# Output: 45.9

# Q19. Float division vs floor division
# Input: 7 / 2 and 7 // 2
# Output: 3.5 and 3

# Q20. Mixed type addition
# Input: 5 + True
# Output: 6

# Q21. Mixed type subtraction
# Input: 10 - False
# Output: 10

# Q22. Complex addition
# Input: (2+3j) + (1+7j)
# Output: 3+10j

if __name__ == "__main__":
    a = 10
    b = 2.5
    print(a + b)

    a, b = "hello", "World"
    print(a+b)

    a = "hi"
    print(a*3)

    booleanV = True and False
    print(booleanV)

    booleanV = True or False
    print(booleanV)

    booleanV = not True
    print(booleanV)

    a = 5 + 3.5
    print(a)

    a = float("45.9")
    print(a)

    a, b = 7/2, 7//2
    print(a,"and", b)

    a, b = 5, True
    print(a+b)

    a, b = 10, False
    print(a-b)

    a, b = (2+3j), (1+7j)
    print(a+b)