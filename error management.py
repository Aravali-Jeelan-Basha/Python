try:
    file1=open('file21.txt','w')
    while True:
        line=file1.readline()
        if line=="":
            break
        print(line)
except:
    print("file not found")
finally:
    print("try except finally")