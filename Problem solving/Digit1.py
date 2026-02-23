class Digit:
    # Count number of digits in a number
    def count_digit(self, num):
        print(num)
        result = 0
        while num > 0:
            result += 1
            num = int(num / 10)
        return result
    
    # Sum of digits of a number
    def sum_digit(self, num):
        sum = 0
        while num > 0:
            digit = int(num % 10)
            sum += digit
            num = num // 10
        return sum

    # Reverse digits of a number
    def reverse_num(self, num):
        num = str(num)
        num = num[::-1]
        return int(num)

    # Check whether a number is palindrome
    def is_palindrome(self, num):
        temp = str(num)[::-1]
        return num == int(temp)

    # Find largest digit in a number & Find smallest digit in a number
    def mm(self, num):
        min, max = None, None
        while num > 0:
            digit = int(num % 10)
            if  max is None or digit > max:
                max = digit
            if min is None or digit < min:
                min = digit
            num = num // 10
        return min, max

    # Count even and odd digits
    def count_even_odd_digit(self, num):
        even, odd = 0, 0
        while num > 0:
            digit = int(num % 10)
            if digit % 2 == 0:
                even += 1
            else:
                odd += 1
            num = num // 10
        return odd, even
    
    # Count frequency of a specific digit
    def count_frequency(self, num):
        frequency = {x:0 for x in range(0, 10)}

        while num > 0:
            digit = int(num % 10)
            frequency.update({digit : frequency.get(digit) + 1})
            num = num // 10
        return frequency
    
    # Check whether number contains digit 0
    def is_zero(self, num):
        while num > 0:
            digit = int(num % 10)
            if digit == 0:
                return True
            num = num // 10
        return False
    
    # Difference between sum of even and odd digits
    def sum_differ_even_odd(self, num):
        even, odd = self.count_even_odd_digit(num)
        sum = even - odd
        if sum < 0:
            sum = -sum
        return sum
    
    # Check whether digits are in ascending order
    def is_digit_ascending(self, num):
        num = str(num)
        for i in range(len(num) - 1):
            if num[i] > num[i+1]:
                return False
        return True
    
    # Check whether digits are in descending order
    def is_digit_descending(self, num):
        num = str(num)
        for i in range(len(num) - 1):
            if num[i] < num[i+1]:
                return False
        return True
    
    # Replace all 0 digits with 1
    def Replace_zero(self, num, replace_with = 1):
        # num = str(num).replace('0','1')
        # return int(num)
        
        new_num = ""
        while num > 0:
            digit = int(num%10)
            if digit == 0:
                digit = 1
            new_num += str(digit)
            num = num // 10
        return int(new_num[::-1])
    
    # Remove all repeated digits
    def remove_duplicate_digit(self, num):
        num = str(num)
        new_num = ""

        for i in range(len(num)):
            if not str(num[i]) in new_num:
                new_num += num[i]
        return int(new_num)

    # Convert digits into words
    def digit_to_word(self, num):
        num_dict = {0:"zero", 1:"one", 2:"zero", 3:"one", 4:"zero", 5:"one", 6:"zero", 7:"one", 8:"zero", 9:"one"}

        words = ""
        while num > 0:
            digit = int(num%10)
            words += num_dict.get(digit) + "-"
            num = num // 10  
        return words      

def main():
    ret = 0
    digit_obj = Digit()

    num = 123605400

    ret = digit_obj.count_digit(num)
    print("The total digits in num is:",ret)

    ret = digit_obj.sum_digit(num)
    print("The sum of digit is:",ret)

    ret = digit_obj.reverse_num(num)
    print("The reverse:",ret)

    num = 101
    ret = digit_obj.is_palindrome(num)
    if ret:
        print("Number is Palindrome")
    else:
        print("Number is not palindrome!!")
    
    num = 192
    ret = digit_obj.mm(num)
    print(f"The min digit is {ret[0]} & The max digit is {ret[1]}")

    ret = digit_obj.count_even_odd_digit(num)
    print(f"The odd count of digit is: {ret[0]} & The even count of digit is: {ret[1]}")

    num = 123122345678998767890
    ret = digit_obj.count_frequency(num)
    print(f"The frequency of digits: {ret}")

    ret = digit_obj.is_zero(num)
    if ret:
        print("The number contain zero")
    else:
        print("The number has no zero!!")

    num = 24681
    ret = digit_obj.sum_differ_even_odd(num)
    print("The Difference between sum of even and odd digits is:",ret)

    num = 12345
    ret = digit_obj.is_digit_ascending(num)
    if ret:
        print("Digits are in ascending order.")
    else:
        print("Digit is not in ascending order.")

    num = 54321
    ret = digit_obj.is_digit_descending(num)
    if ret:
        print("Digits are in descending order.")
    else:
        print("Digit is not in descending order.")

    num = 1010220
    ret = digit_obj.Replace_zero(num)
    print(f"old_num: {num} & new_num: {ret}")

    ret = digit_obj.remove_duplicate_digit(num)
    print(f"The old_num: {num}, Now after removing duplicate digit: {ret}")

    ret = digit_obj.digit_to_word(num)
    print(f"The num is: {num}\nThe word is:{ret}")

if __name__ == "__main__":
    main()