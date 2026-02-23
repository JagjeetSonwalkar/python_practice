
class Digit:
    # is_palindrome number:
    def is_palindrome(self, num):
        temp = str(num)[::-1]
        return num == int(temp)

    # Find next palindrome number
    def next_palindrome(self, num):
        if self.is_palindrome(num):
            i = num
            while True:
                i += 1
                if self.is_palindrome(i):
                    return i
        else:
            return False
    
    # Find previous palindrome number
    def prev_palindrome(self, num):
        if self.is_palindrome(num):
            i = num
            while num >= 0:
                i -= 1
                if self.is_palindrome(i):
                    return i
        else:
            return False

    #Rearrange digits to form largest possible number
    def larg_num(self, num):
        num_list = []
        for i in str(num):
            num_list.append(i)
        num_list.sort(reverse=True)
        value = ""
        for i in num_list:
            value += i
        return int(value)

    # Rearrange digits to form smallest possible number
    def small_num(self, num):
        num_list = []
        for i in str(num):
            num_list.append(i)
        num_list.sort()
        value = ""
        for i in num_list:
            value += i
        return int(value)
    
    # Count all substrings of digits divisible by 3
    def count_substrings(self, num, divisible = 3):
        count = 0
        while num > 0:
            digit = num % 10
            if digit % divisible == 0:
                count += 1
            num = num / 10
        return count
        



def main():
    ret = 0
    obj = Digit()
    num = 2529

    ret = obj.next_palindrome(num)
    print(f"The current palindrome no. is {num} & next palindrome number is: {ret}")

    ret = obj.prev_palindrome(num)
    print(f"The current palindrome no. is {num} & prev palindrome number is: {ret}")

    ret = obj.larg_num(num)
    print(f"The current no. is {num} & from this number largest number is: {ret}")

    ret = obj.small_num(num)
    print(f"The current no. is {num} & from this number smallest number is: {ret}")

    ret = obj.count_substrings(num, divisible=3)
    print(f"{num}, & the Count all substrings of digits divisible by 3 is: {ret}")

if __name__ == "__main__":
    main()