with open('FileIO.txt') as f:           # Automatically closes the file as well, no need of f.close()
    a=f.read(7)
    print(a)