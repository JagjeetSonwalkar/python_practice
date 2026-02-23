# Q32. Get binary representation of int
# Input: 10
# Output: 0b1010

# Q33. Get octal representation of int
# Input: 10
# Output: 0o12

# Q34. Get hexadecimal representation of int
# Input: 10
# Output: 0xa

# Q35. Convert binary string to int
# Input: "1010" base=2
# Output: 10

# Q36. Convert octal string to int
# Input: "12" base=8
# Output: 10

# Q37. Convert hex string to int
# Input: "a" base=16
# Output: 10

# Q38. Float precision formatting
# Input: 3.14159 → round to 2 decimal
# Output: 3.14

# Q39. Large int handling
# Input: 123456789123456789 * 10
# Output: 1234567891234567890

# Q40. Convert list to tuple
# Input: [1,2,3]
# Output: (1,2,3)

if __name__ == "__main__":
    a = 10
    print(bin(a))

    a = 10
    print(oct(a))

    a = 10
    print(hex(a))

    a = "1010"
    base = 2
    intValue = int(a, base)
    print(intValue)

    a = "12"
    base = 8
    intValue = int(a, base)
    print(intValue)

    a = 3.14159
    a = round(a, 2)
    print(a)

    a = 123456789123456789 * 10
    print(a)

    li = [1,2,3]
    li = tuple(li)
    print(li)