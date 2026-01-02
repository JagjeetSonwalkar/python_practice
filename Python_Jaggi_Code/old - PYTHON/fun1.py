# Input: 17 → Output: Next Prime = 19 (function next_prime(n))

def nextPrime(num):
    result = 1
    for i in range(1,num+1,1):
        result *= i
    print(result)

def main():
    no = 17

    Ret = nextPrime(no)

if __name__ == "__main__":
    main()
