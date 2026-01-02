# Q41. Nested type conversion
# Input: int(float("99.9"))
# Output: 99

# Q42. Evaluate mixed type expression
# Input: 5 + 2.5 * 2 - True
# Output: 9.0

# Q43. Swap variables without third variable
# Input: a=5, b=7
# Output: a=7, b=5

# Q44. Detect data type dynamically
# Input: "Python", 99, 5.5, True
# Output: str, int, float, bool

# Q45. Complex number conjugate
# Input: 5+3j
# Output: 5-3j

# Q46. Convert int → binary → int
# Input: 13 → bin → int
# Output: 13

# Q47. Find size in bytes of int
# Input: sys.getsizeof(1000)
# Output: (depends on system, e.g., 28)

# Q48. Convert list of strings to list of int's
# Input: ["1","2","3"]
# Output: [1,2,3]

# Q49. Nested conversion (tuple→list→set)
# Input: (1,2,2,3)
# Output: {1,2,3}

# Q50. Type casting chain
# Input: float(int("123"))
# Output: 123.0

import sys

def detectdataType(value):
    for i in value:
        print(type(i),end=",")
    print()

if __name__ == "__main__":
    a = 99.9
    a = int(a)
    print(a)

    a = 5 + 2.5 * 2 - True
    print(a)

    a = 5
    b = 7
    a, b = b, a
    print("a=",a,"b=",b)

    a = "Python", 99, 5.5, True
    detectdataType(a)

    a = 5+3j
    a = a.conjugate()
    print(a)

    a = 13
    print(a,"->",end="")
    a = bin(a)
    print(a,"->",end="")
    base = 2
    a = int(a, base)
    print(a,end="")
    print()

    a = 1000
    size = int(sys.getsizeof(a))
    print(size)

    a = ["1","2","3"]
    a = [int(i) for i in a]
    print(a)

    a = (1,2,2,3)
    print(type(a),end="->")
    a = list(a)
    print(type(a),end="->")
    a = set(a)
    print(type(a),end="->")
    print()

    a = 123
    a = float(a)
    print(a)