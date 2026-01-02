# Find Sum of First N Even Numbers
# Input 1 → 5 → Output 1 → 30
# Input 2 → 3 → Output 2 → 12

# Find Sum of First N Odd Numbers
# Input 1 → 5 → Output 1 → 25
# Input 2 → 4 → Output 2 → 16

# Check if Two Numbers are Co-Prime
# Input 1 → 12, 25 → Output 1 → True
# Input 2 → 12, 18 → Output 2 → False

def getSumOfEvenNumber(iRange):
    nEvenNum, num, iSum = 0, 0, 0
    while(nEvenNum <= iRange):
        if(num % 2 == 0):
            iSum += num
            nEvenNum += 1
        num += 1
    return iSum

def getSumOfOddNumber(iRange):
    nOddNum, num, iSum = 0, 0, 0

    while(nOddNum < iRange):
        if(num % 2 == 1):
            iSum += num
            nOddNum += 1
        num += 1
    return iSum

def isCoPrime()

def main():
    num = 0
    solution = 0

    num = int(input("Enter the number to find the sum of n even number: "))
    solution = getSumOfEvenNumber(num)
    print("Sum of first n:",num," Even Numbers is: ",solution)

    num = int(input("Enter the number to find the sum of n odd number: "))
    solution = getSumOfOddNumber(num)
    print("Sum of first n:",num," Odd Numbers is: ",solution)

if __name__ == "__main__":
    main()