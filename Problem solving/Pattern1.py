# Print Pattern: Right-angled Triangle
# *
# **
# ***

# Print Pattern: Inverted Triangle
# ***
# **
# *

# Print Multiplication Table for Range 1 to N
# Input 1 → 3 → Output 1 →
# 1 2 3
# 2 4 6
# 3 6 9
# Input 2 → 2 → Output 2 →
# 1 2
# 2 4


def rightAngledTriangle(getFrequency):
    for i in range(1,getFrequency+1):
        print(i*'*',end="")
        print()

def invertedTriangle(getFrequency):
    for i in range(getFrequency,0,-1):
        print(i*'*',end="")
        print()

def multiplicationTable(getRow, getCol):
    for i in range(1, getRow+1):
        for j in range(1, getCol+1):
            print(j*i,end=" ")
        print()

def main():
    rightAngledTriangle(3)

    print()

    invertedTriangle(3)

    print()

    multiplicationTable(3, 3)

if __name__ == "__main__":
    main()