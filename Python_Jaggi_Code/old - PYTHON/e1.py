# validat user input exercise
'''
1. username is no more than 12 characters
2. username must not contain spaces
3. username must not conatin digits
'''

import string

def is_validate(username):
    if len(username) > 12:
        return "username is no more than 12 characters!"
    if " " in username:
        return "username must not contain spaces!"
    if not username.isalpha():
        return "username must not conatin digits!"
    return True

def validate(username):
    if " " in username:
        username = username.replace(" ","")
    if not username.isalpha():
        new_name = ""
        for char in username:
            if not char.isdigit():
                new_name += char
        username = new_name
    if len(username) > 12:
        username = username[0:12]
    return username

username = input("Enter the username: ")

# ret = is_validate(username)

# if ret != True:
#     print(ret)
# else:
#     print("username is valid")

username = validate(username)
print(f"user name is {username}")

