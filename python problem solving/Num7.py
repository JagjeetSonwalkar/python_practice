# display the factors of a number
# check perfect Number
# chech prime Number

def displayFactor(getNum):
    for i in range(1,(getNum+1)//2,1):
        if getNum % i == 0:
            print(i,end=", ")
    print()

def isPerfectNum(getNum):
    iSum = 0
    for i in range(1,getNum):
        if getNum % i == 0:
            iSum += i
    return getNum == iSum

def isPrime(getNum):
    for i in range(2,int(getNum**0.5)+1):
        if getNum % i == 0:
            return False
    return True

def main():
    bRet = False

    displayFactor(50)
    isPerfectNum(6)
    bRet = isPrime(2)
    if(bRet == True):
        print("its a prime Number")
    else:
        print("it is not a prime number")

if __name__ == "__main__":
    main()