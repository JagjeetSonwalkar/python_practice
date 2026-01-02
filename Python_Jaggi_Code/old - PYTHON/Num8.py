# Sum of Digits Raised to Their Positions
# Input 1 → 123 → Output 1 → 1^1 + 2^2 + 3^3 = 32
# Input 2 → 321 → Output 2 → 3^1 + 2^2 + 1^3 = 8

#  Find LCM of Two Numbers
# Input 1 → 4, 6 → Output 1 → 12
# Input 2 → 5, 10 → Output 2 → 10

def sumOfDigitsRaised(getNum):
    i = 1
    iResult = 0
    while(getNum != 0):
        iDigit = getNum % 10
        iResult += (iDigit**iDigit)
        getNum //= 10
    return iResult

def getGCD(Num1, Num2):
    while(Num2):
        Num1, Num2 = Num2, Num1 % Num2
    return Num1

def getLCM(Num1, Num2):
    LCM = 0
    LCM = (Num1 * Num2) // (getGCD(Num1, Num2))
    return LCM

def main():

    Ret = 0
    Ret = sumOfDigitsRaised(123)
    print(Ret)

    Ret = getLCM(4,6)
    print("LCM: ",Ret)

if __name__ == "__main__":
    main()