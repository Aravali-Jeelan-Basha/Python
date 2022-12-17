

import re
def passwordcheck(password):
    if (re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*])[a-zA-Z\d@#$%^&*]{6,20}", password)):
        print("Invalid password")
    else:
        print("valid password")


print("your username")
username = input()
print("your email")
email = input()
print("your password")
password = input()
if (re.match(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email)):
    print("valid email")
else:
    print("Invalid email")
passwordcheck(password)