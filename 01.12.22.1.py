import re
def validemail(email):
    if(re.match(r"\b[a-zA-z0-9._%+-]+@[a-zA-z0-9.-]+\.[a-zA-z]{2,}\b",email)):
        return "valid email"+email
    else:
        return "not valid email"+email
file1=open("file1.txt",'r')
while True:
        line=file1.readline()
        if line=="":
            break
        line=line[:-1]
        print(validemail(line))
file1.close()