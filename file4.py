try:
    inf=open("file4.txt")
    for i in inf:
        output=i.title()
        print(output)

    
    inf.close()
except IOError as io:
    print(io)
