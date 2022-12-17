import re
print('your username')
username=input()
print('your email')
email=input()
print('your password')
password=input()
if(re.match(r'\b[a-zA-z0-9._%+-]+@[a-zA-z0-9]+\.[a-zA-z]{2,},',email)):
    print('.valid email')
else:
    print('valid email')
    if(re.match(r'^(?=*[A-Z])9?=.*[a-z](?=.*\d)(?=.*[@#$%^&*])[a-zA-z\d@#$%^&*]{6,20}',password)):
        print('Invalid password')
    else:
        print('valid password')