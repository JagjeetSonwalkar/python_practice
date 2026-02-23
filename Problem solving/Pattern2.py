# Print Number Pyramid Pattern
# Input 2 → 5 → Output 2 →
# 1
# 12
# 123
# 1234
# 12345

# Print Alphabet Pattern Using Loops
# Input 2 → 5 → Output 2 →
# A
# AB
# ABC
# ABCD
# ABCDE

# Print Diamond Pattern of Stars
# Input 2 → 4 → Output 2 →
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

def numberPyramid(getNum):
    for i in range(1, getNum+1):
        for j in range(1, i+1):
            print(j,end="")
        print()

def alphabetPyramid(getNum):
    for i in range(1, getNum+1):
        for j in range(1, i+1):
            print(chr(64+j),end="")
        print()

def diamond(getNum):
    for i in range(1,getNum+1):
            print(" " * (getNum-i) + "*" * (2*i-1))
    for i in range(getNum-1,0,-1):
            print(" " * (getNum-i) + "*" * (2*i-1))
    

def main():
    numberPyramid(5)

    print()

    alphabetPyramid(5)

    print()

    diamond(4)

if __name__ == "__main__":
    main()