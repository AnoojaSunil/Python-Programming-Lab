try:
    a=open("abc.txt","a")
    s=input("Enter the text:")
    while s:
        a.write(s+"\n")
        s=input("Enter the text:")
    a.close()

except IOError as io:
    print(io)
        
