# Print binary of input number

if __name__ == "__main__":
    no = 0
    no = int(input("Enter number: "))

    print(f"Binary of number {no} is:",bin(no))     # with 0b
    print(f"Binary of number {no} is:",bin(no)[2:]) # without 0b