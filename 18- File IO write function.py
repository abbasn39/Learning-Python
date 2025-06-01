# f= open("FileIO.txt","w")                   # Opens the file in write mode specified using 'w'
# f.write("What does the fox say?")           # This writes everything in the file by the "What does the fox say?" string
# f.close()                                   # Everything in the file previously is removed due to 'w' function

# x=open("IO writing function experiment file.txt","w")   # File created if it doesn't already exist.
# x.write("Abbas is a boy")
# x.close()

# x= open("IO writing function experiment file.txt","a")
# a=x.write("This is a new line")               # appends new string to the file.
# print(a)                                      # This will print the number of new characters printed (18 in this case)
# x.close()
# Whenever the above lines are executed the mentioned string will append to the file.


q=open("FileIO.txt","r+")                               # This is 'read' & 'write' mode
print(q.read())                                         # Output= What's already in the file
q.write("I'm adding this line to check the r+ mode")
q.close()
# Note that 'r+' mode does  not clear the file even though its also write mode.
# q.read() moves the pointer to the end, and if you write anything then it is added in the end.
# q.seek(0) can be used to move the pointer to the start and q.write will then start replacing string indices.
# Remember: 'r+' mode writes at pointer position while only 'w' writes the whole thing.


#   | Mode   | Read  | Write  | Overwrites         | Creates File  |
#   |--------| ------|--------| ------------------ |---------------|
#   | `'r'`  | ✅    | ❌     | ❌                | ❌            |
#   | `'w'`  | ❌    | ✅     | ✅ (deletes all)  | ✅            |
#   | `'a'`  | ❌    | ✅     | ❌ (adds to end)  | ✅            |
#   | `'r+'` | ✅    | ✅     | ✅ (from cursor)  | ❌            |
