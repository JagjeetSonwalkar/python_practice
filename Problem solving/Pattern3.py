# Hollow Square Pattern
# ****
# *  *
# *  *
# ****

# Numbers in Reverse Order per Row
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

def hollowSquare(size):
    for i in range(1,size+1):
        for j in range(1, size+1):
            if i==1 or j==1 or i == size or j == size:
                print('*',end="")
            else:
                print(' ',end="")
        print()

def reverseOrderRow(getSize):
    for i in range(1, getSize+1):
        for j in range(1, (getSize+1)-i+1):
            print(j,end=" ")
        print()


def main():
    hollowSquare(4)

    print()

    reverseOrderRow(5)

if __name__ == "__main__":
    main()