try:
    inf=open("file3.txt")
    words=inf.read().split()
    maxlen=len(max(words,key=len))
    for word in words:
        if len(word)==maxlen:
            print("Longest word :",word)

    inf.close()
except IOError as io:
    print(io)
