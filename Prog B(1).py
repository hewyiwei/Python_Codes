# CA2 Programming Q B
# Checking the validity of password
# This solution delivers more than what the question requires.
# It gives info about every invalid case, why the password is invalid.

psw = input("Enter password: ")
digit = 0  # Initialisation
UC = 0
lc = 0
space = 0

valid = True   # Assume valid first

if len(psw)<6:  # check length
    print("Invalid. Less than 6 characters.")
    valid = False
elif len(psw)>20:
    print("Invalid. More than 20 characters.")
    valid = False

for c in psw:  # check the characters individually
    if c == " ":
        space += 1
    elif c.isdigit():
        digit += 1
    elif c.isupper():
        UC += 1
    elif c.islower():
        lc += 1

# finished checking all the characters
if space > 0:
    print("Invalid. Password contains", space, " spaces.")
    valid = False
if digit == 0:
    print("Invalid. No digit in the password")
    valid = False
if UC == 0:
    print("Invalid. No uppercase letter in the password")
    valid = False
if lc == 0:
    print("Invalid. No lowercase letter in the password")
    valid = False

if valid:
    print("Valid password.")

