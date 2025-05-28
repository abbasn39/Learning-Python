#           Mode            Description

#           'r'	            Read (default) – file must exist
#               'rb'        Read in binary format
#               'rt'        Read in text format (Default mode, same as 'r')
#           'w'	            Write – creates a new file or overwrites existing
#           'a'	            Append – adds to the end of file
#           'x'	            Create – fails if file exists
#           'b'	            Binary mode (e.g., 'rb', 'wb')
#           't'	            Text mode (default, e.g., 'rt')


#open("FileIO.txt")                  #This only opens the file
print("\nFILE OPENED, READ AND CLOSED\n")
f= open("FileIO.txt","r")           # File opened and stored in f. File would still open in read mode even without "r"
                                    # "r" is the second argument and specifies the mode file opens in.(Read mode here)
content= f.read()                   # File opened in read mode(text mode by default) and stored in content
print(content)
f.close()                           # Closes the file(Good practice to close a file)

print("\nREADING CHARACTERS\n")
a=open("FileIO.txt")
x=a.read(3)                         # reads the first 3 characters only
print(x)

y=a.read(5)                         # reads the NEXT 5 characters
print(y)
a.close()


print("\nREADING ALL CHARACTERS AND 2 PRINT STATEMENTS\n")

a=open("FileIO.txt")
x=a.read(4583434)                           # reads all the characters
print("\nFirst print statement\n",x)

x=a.read(5)                                 # reads the NEXT 5 characters
print("\nSecond print statement\n",x)       # This will print nothing as all the characters are already
                                            # printed in first print statement
a.close()

print("\nFOR STATEMENTS\n")
a=open("FileIO.txt")
#content=a.read()                           #<---If content=a.read() line is in the code then the next print will
                                            #  have nothing to show
for line in a:
    print(line,end='')
a.close()

print("\nREADLINE\n")
a=open("FileIO.txt")
print(a.readline())                         # Prints 1st line in text file, also reads the \n character in file.
print(a.readline())                         # Prints 2nd line in text file, also reads the \n character in file.
a.close()

print("\nREADLINES\n")
a=open("FileIO.txt")
print(a.readlines())                        #Prints all the lines as a list, notice the \n characters in the list.
a.close()
