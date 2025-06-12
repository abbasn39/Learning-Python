# f=open("FileIO.txt")
# print(f.tell())                 # This will tell the index where the pointer is at.
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()



f=open("FileIO.txt")
print(f.readline())
f.seek(2)                   # Moves the pointer to the mentioned seek position(seek explanation below)
print(f.tell())             # Prints the current position of pointer which is 2 as set in L
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

# Line              A b b a s
#                  ^ ^ ^ ^ ^ ^
# Seek Position    0 1 2 3 4 5