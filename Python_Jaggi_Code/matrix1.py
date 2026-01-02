# Input: 3 4 → Output:
# Matrix:
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12

def main():
    row = int(input("Enter the row size: "))
    col = int(input("Enter the col size: "))

    list = []
    iRun = 0

    for i in range(1,row+1):
        newlist = []
        for j in range(1,col+1):
            iRun += 1
            newlist.append(iRun)
        list.append(newlist)
    
    for i in list:
        print(i)


if __name__ == "__main__":
    main()