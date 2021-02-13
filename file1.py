try:
    word=input("Enter the word:");
    inf=open("file1.txt")
    lines=inf.readlines()
    inf.close()
    outf=open("filee1.txt","w")
    for line in lines:
        if word not in line.strip("\n"):
            outf.write(line)

    outf.close()
except IOError as io:
    print(io)
    
