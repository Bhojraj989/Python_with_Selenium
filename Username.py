# Validate user input exercise
# 1. username is no more 12 characters.
# 2. Username must not contain any spaces.
# 3. Username must mot contain digits.

username = input("Enter the username you want to create : ")

if len(username) > 12:
    print("The length of the username can't be greater than 12 letters")
elif not username.find(" ") == -1:
    print("Username should not have any spaces.")
elif not username.isalpha():
    print("Username should not have any digits.")
else :
    print(f"Welcome {username}!!")

