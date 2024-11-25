import re

# read username and password from keyboard
username = input('Enter username: ')
password = input('Enter password: ')

# pattern (criteria) for username and password
username_pattern = "[a-z]{5}[a-z]+"
password_pattern = "^(?=.*?[A-Z])?(?=.*?[a-z])(?=.*?[0-9])?(?=.*?[_])?.{8,}$"

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
print(username_match)
print(password_match)
if username_match and password_match:
   print("Great")
else:
   print("Too bad")